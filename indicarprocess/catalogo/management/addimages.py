# -*- coding: utf-8 -*-
from datetime import date

from django.core.management.base import BaseCommand

from imagery.models import Image

from ...tasks import add_image


class Command(BaseCommand):
    help = """Add RGB images to CatalogoLandsat and generate the TMS."""

    def handle(self, *args, **options):
        for image in Image.objects.filter(type='r6g5b4', date__gte=date.today()):
            add_image(image)