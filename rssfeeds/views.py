from django.shortcuts import render

from rssfeeds.models import Category, RssFeeds, NewsFeeds
import feedparser


def add_rss(request):
    pass

def store_new_story(stories):
    for story in stories:
        hash_id = hash(story.link)
        try:
            ex_story = NewsFeeds.objects.get(hash_id=hash_id)
            if not category in ex_story.categories.all():
                ex_story.categories.add(category)
                ex_story.save()
        except ObjectDoesNotExist:
            
def start_crawl():
    feeds = RssFeeds.objects.all()
    for feed in feeds:
        fp = None
        try:
            fp = feedparser.parse(feed.rss)
            if fp.status != 200 and fb.bozo:
                raise Exception('Can not reach rss')
            if len(fb.entries) == 0:
                raise Exception('Empty Rss or Invalid Rss')

        except Exception as e:
            feed.is_active = False
            feed.status = e.formatexc()
            feed.save()
            continue
        if feed.updated < fp.updated:
            feed.updated = fp.updated
            feed.status = store_new_stroy(fb.entries, feed.category)
            feed.is_active = True
