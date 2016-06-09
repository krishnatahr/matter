from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    country = models.CharField(max_length=10)

class RssFeeds(models.Model):
    category = models.ForeignKey(Category)
    rss = models.CharField(max_length=600)
    source = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    language = models.CharField(max_length=50)
    updated = models.DateTimeField()
    publised = models.DateTimeField()

class NewsFeeds(models.Model):
    title = models.CharField(max_length=600)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    link_url = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    puplished = models.DateTimeField()
    hash_id = models.CharField(max_length=32)
    category = models.ForeignKey(category)
