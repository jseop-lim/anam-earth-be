from django.conf import settings
from django.db import models


class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.DO_NOTHING)  # TODO user
    username = models.CharField(verbose_name='작성자 이름', max_length=150)
    subject = models.CharField(verbose_name='게시물 제목', max_length=255)
    content = models.TextField(verbose_name='게시물 내용')
    created_at = models.DateTimeField(verbose_name='작성 일시', auto_now_add=True)


class Comment(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.DO_NOTHING)  # TODO user
    username = models.CharField(verbose_name='작성자 이름', max_length=150)
    post = models.ForeignKey(verbose_name='게시물', to='Post', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='댓글 내용')
    created_at = models.DateTimeField(verbose_name='작성 일시', auto_now_add=True)
