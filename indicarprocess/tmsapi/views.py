from rest_framework.generics import ListAPIView, RetrieveAPIView

from catalogo.models import CatalogoLandsat, CatalogoRapidEye
from .serializers import LandsatSerializer, RapidEyeSerializer


class LandsatListAPI(ListAPIView):
    serializer_class = LandsatSerializer

    def get_queryset(self):
        bbox = self.request.query_params.get('extent', None)
        if bbox:
            return CatalogoLandsat.objects.filter(geom__intersects=bbox).order_by('data')
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


class LandsatDetailView(RetrieveAPIView):
    queryset = CatalogoLandsat.objects.all()
    serializer_class = LandsatSerializer
    lookup_field = 'image'


class RapidEyeDetailView(RetrieveAPIView):
    queryset = CatalogoRapidEye.objects.all()
    serializer_class = RapidEyeSerializer
    lookup_field = 'image'

