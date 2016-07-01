from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.CharField(max_length=64, blank=True, null=True)
    country = models.CharField(max_length=10)


class RssFeed(models.Model):
    category = models.ForeignKey(Category)
    rss = models.CharField(max_length=600)
    source = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    publised = models.DateTimeField(blank=True, null=True)

    class Meta:
        table = 'rssfeeds'

class NewsFeed(models.Model):
    title = models.CharField(max_length=600)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    link_url = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    puplished = models.DateTimeField()
    hash_id = models.CharField(max_length=32)
    rss = models.ForeignKey(RssFeed)
    categories = models.OneToMeny(Category)

    class Meta:
        table = 'news'
