# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from catalogo.models import CatalogoLandsat, CatalogoRapidEye


class LandsatSerializer(ModelSerializer):
    southwest = SerializerMethodField()
    northeast = SerializerMethodField()
    name = SerializerMethodField()

    class Meta:
        model = CatalogoLandsat
        fields = ['name', 'data', 'southwest', 'northeast']

    def get_bounds(self, obj):
        lats = []
        lons = []
        for lat, lon in obj.geom.coords[0][0]:
            lats.append(lat)
            lons.append(lon)

        lats.sort()
        lons.sort()
        return [[lats[-1], lons[-1]], [lats[0], lons[0]]]

    def get_southwest(self, obj):
        return self.get_bounds(obj)[-1]

    def get_northeast(self, obj):
        return self.get_bounds(obj)[0]

    def get_name(self, obj):
        return obj.image.replace('.tif', '')


class RapidEyeSerializer(ModelSerializer):
    southwest = SerializerMethodField()
    northeast = SerializerMethodField()
    name = SerializerMethodField()

    class Meta:
        model = CatalogoRapidEye
        fields = ['name', 'data', 'southwest', 'northeast']

    def get_bounds(self, obj):
        lats = []
        lons = []
        for lat, lon in obj.geom.coords[0][0]:
            lats.append(lat)
            lons.append(lon)

        lats.sort()
        lons.sort()
        return [[lats[-1], lons[-1]], [lats[0], lons[0]]]

    def get_southwest(self, obj):
        return self.get_bounds(obj)[-1]

    def get_northeast(self, obj):
        return self.get_bounds(obj)[0]

    def get_name(self, obj):
        return obj.image.replace('.tif', '')
