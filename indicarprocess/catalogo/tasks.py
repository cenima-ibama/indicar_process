## -*- coding: utf-8 -*-
import logging
from os import environ
from subprocess import call
from createhdr.createhdr import ReadTif
from os.path import join, dirname
from celery import shared_task, group

from django.conf import settings
from django.contrib.gis.geos import MultiPolygon

from imagery.models import Image

from .models import CatalogoLandsat

logger = logging.getLogger(__name__)

BASE_PATH = dirname(__file__)

PATH_TO_SCRIPT = join(BASE_PATH, 'bin/make_tms.sh')
OUTPUT_PNG_PATH = settings.PNG_IMAGES_PATH
OUTPUT_TMS_PATH = settings.TMS_IMAGES_PATH
LINK_BASE = settings.URL_TMS_BASE

environ['PATH'] += ':'+join(BASE_PATH, 'bin/scripts-for-gis')
environ['PATH'] += ':'+join(BASE_PATH, 'bin/tilers-tools.v32/tilers_tools')

@shared_task
def make_tms(image):
    """Generate the TMS of an Image."""

    if (image.type == 'r6g5b4' and image.scene.sat == 'L8') or \
        (image.type == 'r5g4b3' and image.scene.sat in ['L5', 'L7']):

        if CatalogoLandsat.objects.filter(image=image.name).count() == 0:

            logger.debug('Starting process "make_tms" to image %s' % image.name)
            call([PATH_TO_SCRIPT, image.file_path(), OUTPUT_PNG_PATH, OUTPUT_TMS_PATH, LINK_BASE])
            logger.debug('Process "make_tms" to image %s finished ' % image.name)
            CatalogoLandsat.objects.create(
                image=image.name,
                path=settings.LANDSAT_PATH_FORMAT % (image.scene.sat[-1], image.scene.name),
                geom=MultiPolygon(image.scene.geom),
                data=image.scene.date,
                nuvens=image.scene.cloud_rate,
                quicklook=image.scene.quicklook(),
                orbita=image.scene.path,
                ponto=image.scene.row,
                url_tms=join(settings.URL_TMS_BASE, '%s_%s_tms.xml' % (image.scene.name, image.type)))

            # create HDR file for the RGB image
            logger.debug('Starting creation of HDR file to image %s' % image.name)
            tif = ReadTif(image.file_path())
            hdr_name = tif.write_hdr()
            logger.debug('Creation of HDR file to image %s finished' % image.name)
            Image.objects.get_or_create(
                name=hdr_name.split('/')[-1],
                type='hdr',
                scene=image.scene)
        else:
            logger.info('%s already has TMS' % image.name)
    else:
        raise Exception('Image is not a Landsat 8 of r6g5b4 type or a Landsat 5/7 of r5g4b3 type.')

@shared_task
def make_tms_all():
    '''Search by all images that've never been processed, and after call make_tms function
    to process that images'''

    type_list = ['r6g5b4', 'r5g4b3']
    logger.debug('Quering all items from catalogo')
    catalog_images = CatalogoLandsat.objects.values_list('image', flat=True)
    logger.debug('Quering images from imagery that weren\'t begot TMS')
    images = Image.objects.filter(type__in=type_list).exclude(name__in=catalog_images)
    logger.info('Found %s images to make TMS' % images.count())
    group([make_tms.s(image) for image in images])()
    logger.info('Make all TMS completed')

def create_hdr(image):

    if (image.type == 'r6g5b4' and image.scene.sat == 'L8') or \
        (image.type == 'r5g4b3' and image.scene.sat in ['L5', 'L7']):

        tif = ReadTif(image.file_path())
        tif.write_hdr()
