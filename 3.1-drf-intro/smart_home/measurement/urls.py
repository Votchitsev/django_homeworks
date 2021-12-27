from django.urls import path

from measurement.views import SensorView, SingleSensorView, MeasurementView


urlpatterns = [
    path('sensor/', SensorView.as_view()),
    path('sensor/<pk>/', SingleSensorView.as_view()),
    path('measurement/', MeasurementView.as_view()),
]
