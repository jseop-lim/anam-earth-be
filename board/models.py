from django.conf import settings
from django.db import models


class Post(models.Model):
    # TODO null=False
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.DO_NOTHING, null=True)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    # TODO null=False
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.DO_NOTHING, null=True)
    content = models.TextField()
