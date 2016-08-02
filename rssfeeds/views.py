from django.shortcuts import render

from rssfeeds.models import Category, RssFeed, NewsFeed
from django.http.response import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from bs4 import BeautifulSoup
from time import mktime
from datetime import datetime, timedelta
import feedparser
import traceback
import urllib2

def add_rss(request):
    pass

def store_new_story(stories, rss):
    category = rss.category
    count = 0
    for story in stories:
        hash_id = hash(story.link)
        news = None
        try:
            news = NewsFeed.objects.get(hash_id=hash_id)
        except ObjectDoesNotExist:
            news = NewsFeed()
            count += 1
        news.title = story.title
        if rss.image_point and not news.image_url:
            try:
                source = urllib2.urlopen(story.link).read()
                soup = BeautifulSoup(source)
                tag, attr = rss.image_point.split(':') if ':' in rss.image_point else rss.image_point, 'src'
                li = soup.select(tag)
                if li and li[0].get(attr):
                    news.image_url = li[0].get(attr)
            except:
                pass
        else:
            news.image_url = story.image if 'image' in story else ''
        news.link_url = story.link
        news.description = story.summary
        if 'published_parsed' not in story:
            continue
        news.puplished = datetime.fromtimestamp(mktime(story.published_parsed))
        news.hash_id = hash_id
        news.rss = rss
        news.save()
        if not category in news.categories.all():
            news.categories.add(category)
            news.save()
    if count:
        return "%d new stor(%s) added" %(count, 'y' if count==1 else 'ies'), count
    else:
        return 'No new story found', count


def start_crawl(request):
    feeds = RssFeed.objects.all()
    count = 0
    for feed in feeds:
        fp = None
        try:
            fp = feedparser.parse(feed.rss)
            if fp.status != 200 and fp.bozo:
                raise Exception('Can not reach rss')
            if len(fp.entries) == 0:
                raise Exception('Empty Rss or Invalid Rss')
        except Exception as e:
            feed.is_active = False
            print traceback.format_exc()
            feed.status = str(e)
            feed.save()
            continue
        if 'updated_parsed' in fp:
            updated = datetime.fromtimestamp(mktime(fp.updated_parsed))
        else:
            updated = datetime.now() - timedelta(hours=0.25)
        if not feed.updated or feed.updated < updated:
            feed.updated = updated
            feed.status, c = store_new_story(fp.entries, feed)
            feed.is_active = True
            feed.save()
            count += c
    return HttpResponse('%d done' % count)

def list_news(request, country=None, topic=None):
    if country and len(country)==2:
        news = NewsFeed.objects.filter(categories__country__exact=country)
    else:
        news = NewsFeed.objects.all()
        topic = country
    if topic:
        print len(news)
        news = news.filter(title__contains=topic)
    print len(news), country, topic, 20*'*'
    return HttpResponse('%s done' % serialize('json', news))
