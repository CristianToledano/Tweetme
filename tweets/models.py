from __future__ import unicode_literals
from django.conf import global_settings
from django.db import models


class Tweet(models.Model):
    user = models.ForeignKey(global_settings.AUTH_USER_MODEL)
    message = models.TextField(max_length=100)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.message)