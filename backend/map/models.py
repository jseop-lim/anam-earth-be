from django.contrib.gis.db import models


class Node(models.Model):
    name = models.CharField(verbose_name='노드 이름', max_length=255)
    # address = models.CharField(max_length=255)
    location = models.PointField(verbose_name='노드 위치(좌표)', srid=4326)


class Arc(models.Model):
    QUALITY_CHOICES = [('상', '상'), ('중', '중'), ('하', '하')]
    start_node = models.ForeignKey(verbose_name='시작 노드', to='Node', on_delete=models.CASCADE,
                                   related_name='start_arcs')
    end_node = models.ForeignKey(verbose_name='끝 노드', to='Node', on_delete=models.CASCADE,
                                 related_name='end_arcs')
    vertical_distance = models.FloatField(verbose_name='수직 거리')
    horizontal_distance = models.FloatField(verbose_name='수평 거리')
    is_stair = models.BooleanField(verbose_name='계단 여부')
    is_step = models.BooleanField(verbose_name='단차 여부', default=False)
    quality = models.CharField(verbose_name='정성 지표', max_length=255, choices=QUALITY_CHOICES)
