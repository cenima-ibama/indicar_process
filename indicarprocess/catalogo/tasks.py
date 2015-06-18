## -*- coding: utf-8 -*-
from os.path import join
from subprocess import call

from .models import CatalogoLandsat


def add_image(image):
    """Function to add an Image to CatalogoLandsat."""

    if (image.type == 'r6g5b4' and image.scene.sat == 'L8') or \
        (image.type == 'r5g4b3' and image.scene.sat in ['L5', 'L7']):

        if CatalogoLandsat.objects.filter(image=image.name).count() == 0:
            CatalogoLandsat.objects.create(
                image=image.name,
                path=join('/mnt/csr/imagens/landsat%s' % image.scene.sat[-1],
                    image.scene.name),
                shape=image.scene.geom,
                data=image.scene.date,
                url_tms=join('http://10.1.25.66/imagens/tms/landsat',
                    '%s_%s_tms.xml' % (image.scene.name, image.type)
                    )
            )
        else:
            print(('Catalogo Landsat to %s already exists.' % image.name))
    else:
        print('Image is not of r6g5b4 or r5g4b3 type.')


def make_tms(image):
    """Generate the TMS of an Image."""

    if (image.type == 'r6g5b4' and image.scene.sat == 'L8') or \
        (image.type == 'r5g4b3' and image.scene.sat in ['L5', 'L7']):

        if CatalogoLandsat.objects.filter(image=image.name).count() == 0:
            call(['make_tms.sh', image.file_path()])
        else:
            print(('%s already has TMS' % image.name))
    else:
        print('Image is not a Landsat 8 of r6g5b4 type or a Landsat 5/7 of r5g4b3 type.')