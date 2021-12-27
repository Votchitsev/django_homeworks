from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    measuring_temperature = models.IntegerField()
    measuring_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default=None, blank=True, null=True)
