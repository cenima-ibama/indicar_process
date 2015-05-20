from datetime import date

from django.test import TestCase
from django.contrib.gis.geos import Polygon

from imagery.models import Image, Scene

from .models import CatalogoLandsat
from .tasks import add_image


class TestCatalogoLandsat(TestCase):

    def setUp(self):
        self.scene = Scene.objects.create(
            path='001',
            row='001',
            sat='L8',
            date=date(2015, 1, 1),
            name='LC80010012015001LGN00',
            geom=Polygon(((0, 0), (1, 1), (1, 0), (0, 0))),
            cloud_rate=20.3,
            status='downloading'
            )

        self.image = Image.objects.create(
            name='LC80010012015001LGN00_r6g5b4.tif',
            type='r6g5b4',
            scene=self.scene
            )

    def test_create_entry(self):
        add_image(self.image)
        self.assertEqual(CatalogoLandsat.objects.all().count(), 1)
        cl = CatalogoLandsat.objects.all()[0]
        self.assertEqual(cl.image, self.image.name)
        self.assertEqual(cl.shape, self.image.scene.geom)
        self.assertEqual(cl.data, self.image.scene.date)
