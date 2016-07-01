from django.contrib import admin
from rssfeeds.model import Category, RssFeed, NewsFeed


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

class RssAdmin(admin.ModelAdmin):
    class Meta:
        model = RssFeed

class NewsAdmin(admin.ModelAdmin):
    class Meta:
        model = NewsFeed

# Register your models here.
admin.register(CategoryAdmin, Category)
admin.register(RssAdmin, RssFeed)
admin.register(NewsAdmin, NewsFeed)
