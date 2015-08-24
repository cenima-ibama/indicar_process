# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from ...tasks import make_tms_all


class Command(BaseCommand):
    help = """Generate the TMS and add RGB images to CatalogoLandsat."""

    def handle(self, *args, **options):
        make_tms_all()
