from abc import ABC

from rest_framework import serializers

from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['id', 'sensor_id', 'measuring_temperature', 'measuring_date', 'image']


class MeasurementListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ('measuring_temperature', 'measuring_date')


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description')


class SingleSensorSerializer(serializers.ModelSerializer):

    measurements = MeasurementListSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description', 'measurements')
