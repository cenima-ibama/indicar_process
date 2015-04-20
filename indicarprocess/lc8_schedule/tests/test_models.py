from django.test import TestCase

from ..models import ScheduledScene


class TestScheduledScene(TestCase):

    def test_scheduled_scene_creation(self):
        scene = ScheduledScene.objects.create(path='001', row='001')
        self.assertEqual(ScheduledScene.objects.all().count(), 1)
        self.assertEqual(scene.__str__(), 'LC8 001-001')
