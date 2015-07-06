# -*- coding: utf-8 -*-
from datetime import date

from django.core.management.base import BaseCommand

from imagery.models import Image

from ...tasks import add_image, make_tms, create_hdr


class Command(BaseCommand):
    help = """Generate the TMS and add RGB images to CatalogoLandsat."""

    def handle(self, *args, **options):
        for image in Image.objects.filter(type='r6g5b4', creation_date__gte=date.today()):
            make_tms(image)
            add_image(image)
            create_hdr(image)