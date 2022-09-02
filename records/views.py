from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from records.models import UserGlucoseLevels
from records.serializers import UserGlucoseLevelsSerializer


class UserRecords(
    viewsets.GenericViewSet,
    generics.ListAPIView,
    generics.RetrieveAPIView,
    generics.CreateAPIView,
):
    serializer_class = UserGlucoseLevelsSerializer
    queryset = UserGlucoseLevels.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user_id"]

    def get_queryset(self):
        queryset = super().get_queryset()

        start = self.request.query_params.get("start")
        stop = self.request.query_params.get("stop")

        if not start or not stop:
            return queryset
        return queryset.filter(device_timestamp__time__range=[start, stop])
