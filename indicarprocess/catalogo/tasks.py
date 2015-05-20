## -*- coding: utf-8 -*-
from os.path import join

from .models import CatalogoLandsat


def add_image(image):
    CatalogoLandsat.objects.get_or_create(
        image=image.name,
        path=join('/mnt/csr/imagens/landsat8', image.scene.name),
        shape=image.scene.geom,
        data=image.scene.date,
        url_tms=join(
            'http://10.1.25.66/imagens/tms/landsat',
            image.scene.name,
            '_r6g5b4_tms.xml'
        )
    )