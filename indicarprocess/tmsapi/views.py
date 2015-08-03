from rest_framework.generics import ListAPIView

from catalogo.models import CatalogoLandsat
from .serializers import LandsatSerializer


class LandsatListAPI(ListAPIView):
    serializer_class = LandsatSerializer

    def get_queryset(self):
        bbox = self.request.query_params.get('extent', None)
        if bbox:
            return CatalogoLandsat.objects.filter(shape__intersects=bbox)
        else:
            return []