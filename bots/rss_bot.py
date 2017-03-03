import feedreader, settings, time
from datetime import datetime, timezone

def get_feed_items():
    rss_items = []
    feed_data = [feedparser.parse(url) for url in settings.RSS_LIST]

    for feed_provider in feed_data:
        rss_items.append({
                'feed_title': feed_provider['feed']['title'],
                'items': [{
                    'title': i['title'],
                    'url': i['link'],
                    # Following conversion magic provided bei SO: https://stackoverflow.com/a/1697907
                    'published': datetime.fromtimestamp(time.mktime(i['published_parsed'])).replace(tzinfo=timezone.utc)
                } for i in feed_provider['entries']]
            })

    return rss_items
    