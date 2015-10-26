## -*- coding: utf-8 -*-
from createhdr.createhdr import ReadTif

from os.path import join
from subprocess import call

from imagery.models import Image

from .models import CatalogoLandsat


def make_tms(image):
    """Generate the TMS of an Image."""

    if (image.type == 'r6g5b4' and image.scene.sat == 'L8') or \
        (image.type == 'r5g4b3' and image.scene.sat in ['L5', 'L7']):

        if CatalogoLandsat.objects.filter(image=image.name).count() == 0:
            call(['/home/wille/script/scripts-for-gis/make_tms.sh', image.file_path()])
            CatalogoLandsat.objects.create(
                image=image.name,
                path='\\\\10.1.25.66\\b52_imagens\\landsat%s\\%s' % (image.scene.sat[-1], image.scene.name),
                shape=image.scene.geom,
                data=image.scene.date,
                nuvens=image.scene.cloud_rate,
                quicklook=image.scene.quicklook(),
                orbita=image.scene.path,
                ponto=image.scene.row,
                url_tms=join('http://10.1.25.66/imagens/tms/landsat',
                    '%s_%s_tms.xml' % (image.scene.name, image.type)
                    )
            )
            # create HDR file for the RGB image
            tif = ReadTif(image.file_path())
            hdr_name = tif.write_hdr()
            Image.objects.get_or_create(
                name=hdr_name.split('/')[-1],
                type='hdr',
                scene=image.scene
            )
        else:
            print(('%s already has TMS' % image.name))
    else:
        print('Image is not a Landsat 8 of r6g5b4 type or a Landsat 5/7 of r5g4b3 type.')


def make_tms_all():
    images = Image.objects.filter(type__in=['r6g5b4', 'r5g4b3'])
    images = [i for i in images if CatalogoLandsat.objects.filter(image=i.name).count() == 0]
    for image in images:
        make_tms(image)


def create_hdr(image):

    if (image.type == 'r6g5b4' and image.scene.sat == 'L8') or \
        (image.type == 'r5g4b3' and image.scene.sat in ['L5', 'L7']):

        tif = ReadTif(image.file_path())
        tif.write_hdr()