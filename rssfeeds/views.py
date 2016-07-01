from django.shortcuts import render

from rssfeeds.models import Category, RssFeeds, NewsFeeds
import feedparser


def add_rss(request):
    pass

def store_new_story(stories, rss):
    category = rss.category
    count = 0
    for story in stories:
        hash_id = hash(story.link)
        news = None
        try:
            news = NewsFeeds.objects.get(hash_id=hash_id)
        except ObjectDoesNotExist:
            news = NewsFeeds()
            count += 1
        news.title = story.title
        news.image_url = story.image
        news.link_url = story.link
        news.description = story.summary
        news.puplished = story.publised
        news.hash_id = hash_id
        news.rss = rss
        if not category in news.categories.all():
            news.categories.add(category)
        news.save()
    if count:
        return "%d new stor(%s) added" %(count, 'y' if count==1 else 'ies')
    else:
        retunr 'No new story found'


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
            feed.status = store_new_stroy(fb.entries, feed)
            feed.is_active = True
            feed.save()
    
