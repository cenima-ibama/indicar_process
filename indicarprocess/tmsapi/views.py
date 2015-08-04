from rest_framework.generics import ListAPIView

from catalogo.models import CatalogoLandsat, CatalogoRapidEye
from .serializers import LandsatSerializer, RapidEyeSerializer


class LandsatListAPI(ListAPIView):
    serializer_class = LandsatSerializer

    def get_queryset(self):
        bbox = self.request.query_params.get('extent', None)
        if bbox:
            return CatalogoLandsat.objects.filter(shape__intersects=bbox).order_by('data')
        else:
            return []


class RapidEyeListAPI(ListAPIView):
    serializer_class = RapidEyeSerializer

    def get_queryset(self):
        bbox = self.request.query_params.get('extent', None)
        if bbox:
            return CatalogoRapidEye.objects.filter(geom__intersects=bbox).order_by('data')
        else:
            return []