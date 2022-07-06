from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Road(models.Model):
    start_pos = models.ForeignKey('Position', on_delete=models.CASCADE, related_name='start_roads')
    end_pos = models.ForeignKey('Position', on_delete=models.CASCADE, related_name='end_roads')
    gradient = models.FloatField()
    width = models.FloatField()
    is_stair = models.BooleanField()
    flatness = models.CharField(max_length=255, choices=(('상', '상'), ('중', '중'), ('하', '하')))
