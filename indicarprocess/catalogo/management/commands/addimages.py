# -*- coding: utf-8 -*-
from celery import group

from django.core.management.base import BaseCommand

from imagery.models import Image

from ...models import CatalogoLandsat
from ...tasks import make_tms


class Command(BaseCommand):
    help = """Generate the TMS and add RGB images to CatalogoLandsat."""

    def handle(self, *args, **options):
        images = Image.objects.filter(type__in=['r6g5b4', 'r5g4b3'])
        images = [i for i in images if CatalogoLandsat.objects.filter(image=i.name).count() == 0]
        group(make_tms.s(image) for image in images)().get()