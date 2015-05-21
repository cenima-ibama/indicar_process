## -*- coding: utf-8 -*-
from os.path import join
from subprocess import call

from .models import CatalogoLandsat


def add_image(image):
    """Function to add a Image to CatalogoLandsat."""
    CatalogoLandsat.objects.get_or_create(
        image=image.name,
        path=join('/mnt/csr/imagens/landsat8', image.scene.name),
        shape=image.scene.geom,
        data=image.scene.date,
        url_tms=join('http://10.1.25.66/imagens/tms/landsat',
            image.scene.name + '_r6g5b4_tms.xml')
    )


def make_tms(image):
    """Generate the TMS of an Image."""
    if image.type == 'r6g5b4':
        path = join('/csr/imagens/landsat8', image.file_path())
        call(['make_tms.sh', path])
    else:
        print('Image is not of r6g5b4 type.')