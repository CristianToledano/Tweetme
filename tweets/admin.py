# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tweets.models import Tweet
from .forms import TweetModelForm

class TweetModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Tweet
        form = TweetModelForm

admin.site.register(Tweet, TweetModelAdmin)