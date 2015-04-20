from datetime import date, timedelta

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import ScheduledScene


class TestScheduledScene(TestCase):

    def setUp(self):
        self.scene = ScheduledScene.objects.create(path='001', row='001',
            last_date=(date.today() - timedelta(days=17)))

    def test_scheduled_scene_creation(self):
        self.assertEqual(self.scene.__str__(), 'LC8 001-001')

        ScheduledScene.objects.create(path='001', row='002')
        self.assertEqual(ScheduledScene.objects.all().count(), 2)

    def test_validation(self):
        with self.assertRaises(ValidationError):
            ScheduledScene.objects.create(path='001', row='001')