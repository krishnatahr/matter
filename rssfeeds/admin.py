from django.contrib import admin
from rssfeeds.models import Category, RssFeed, NewsFeed


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    pass

class RssAdmin(admin.ModelAdmin):
    pass

class NewsAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Category, CategoryAdmin,)
admin.site.register(RssFeed, RssAdmin)
admin.site.register(NewsFeed, NewsAdmin)
