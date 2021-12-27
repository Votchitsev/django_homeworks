# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView

from measurement.serializers import SensorSerializer, MeasurementSerializer, SingleSensorSerializer
from measurement.models import Sensor, Measurement


class SensorView(ListCreateAPIView, CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SingleSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SingleSensorSerializer


class MeasurementView(CreateAPIView, GenericAPIView, ListModelMixin):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
