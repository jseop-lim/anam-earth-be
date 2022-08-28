from django.contrib.gis.db import models


class Node(models.Model):
    name = models.CharField(verbose_name='노드 이름', max_length=255)
    # address = models.CharField(max_length=255)
    point = models.PointField(verbose_name='노드 위치(좌표)')


class Arc(models.Model):
    QUALITY_CHOICES = [('상', '상'), ('중', '중'), ('하', '하')]
    start_node = models.ForeignKey(verbose_name='출발 노드', to='Node', on_delete=models.CASCADE,
                                   related_name='start_arcs')
    end_node = models.ForeignKey(verbose_name='도착 노드', to='Node', on_delete=models.CASCADE,
                                 related_name='end_arcs')
    vertical_distance = models.FloatField(verbose_name='수직 거리')
    horizontal_distance = models.FloatField(verbose_name='수평 거리')
    is_stair = models.BooleanField(verbose_name='계단 여부')
    is_step = models.BooleanField(verbose_name='단차 여부', default=False)
    quality = models.CharField(verbose_name='정성 지표', max_length=255, choices=QUALITY_CHOICES)

    @property
    def gradient(self) -> float:
        return self.vertical_distance / self.horizontal_distance

    @property
    def level(self) -> int:  # TODO coler string 반환?
        if self.gradient > 0.08 or self.is_stair or self.is_step:
            return 3
        elif self.gradient > 0.055 and self.quality == '하':
            return 2
        else:
            return 1
