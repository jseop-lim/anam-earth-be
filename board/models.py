from django.conf import settings
from django.db import models


class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.DO_NOTHING)  # TODO user
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.DO_NOTHING)  # TODO user
    content = models.TextField()
