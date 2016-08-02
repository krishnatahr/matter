from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32, blank=True, null=True)
    country = models.CharField(max_length=10)
    class Meta:
        db_table = 'categories'

    def __unicode__(self):
        return '%s - %s' % (self.title, self.country)


class RssFeed(models.Model):
    category = models.ForeignKey(Category)
    rss = models.CharField(max_length=600)
    source = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image_point = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    publised = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'rssfeeds'

class NewsFeed(models.Model):
    title = models.CharField(max_length=600)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    link_url = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    puplished = models.DateTimeField()
    hash_id = models.CharField(max_length=32)
    rss = models.ForeignKey(RssFeed)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'news'
