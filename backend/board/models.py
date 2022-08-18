from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserNameField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs.update(
            verbose_name='작성자 이름', max_length=150, unique=True,
            error_messages={"unique": _("A user with that username already exists.")},
        )
        super().__init__(*args, **kwargs)


class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.DO_NOTHING)  # TODO user
    username = UserNameField()
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.DO_NOTHING)  # TODO user
    username = UserNameField()
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
