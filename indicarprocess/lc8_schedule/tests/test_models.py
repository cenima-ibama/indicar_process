from datetime import date, timedelta

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import ScheduledScene


class TestScheduledScene(TestCase):

    def test_scheduled_scene_creation(self):

        scene = ScheduledScene.objects.create(path='001', row='001',
            last_date=(date.today() - timedelta(days=17)))
        self.assertEqual(scene.__str__(), 'LC8 001-001')

        ScheduledScene.objects.create(path='001', row='002')

        with self.assertRaises(ValidationError):
            ScheduledScene.objects.create(path='001', row='001')

        self.assertEqual(ScheduledScene.objects.all().count(), 2)
