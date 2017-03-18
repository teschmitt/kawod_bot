# rename this fucking module when it's clear what it does

import settings, logging, random
from models import *

def prepare_db():
    # these args will probably only work with sqlite.
    db.bind(settings.DB_TYPE, settings.DB_NAME, create_db=True)
    sql_debug(True)
    db.generate_mapping(create_tables=True)

@db_session
def push_to_db(reddit_items=None, newsriver_items=None, rss_items=None):
    commit_list = []
    if reddit_items is not None:
        logging.info('Pushing reddit items to database')
        for r in reddit_items:
            if not is_dupe(item=r, item_type='reddit_item'):
                commit_list.append(
                    RedditEntry(
                        reddit_id = r['reddit_id'],
                        score = r['score'],
                        subreddit = r['subreddit'],
                        author = r['author'],
                        title = r['title'],
                        url = r['url'],
                        timestamp = r['timestamp'],
                        published = False
                    )
                )
            else:
                logging.info('Reddit ID {} is a duplicate and already included in DB. Removed from commit stack.'.format(r['reddit_id']))
    else:
        logging.info('No reddit items available to push to database')
    if newsriver_items is not None:
        logging.info('Pushing newsriver items to database')
        for n in newsriver_items:
            if not is_dupe(item=n, item_type='newsriver_item'):
                commit_list.append(
                    NewsriverEntry(
                        title = n['title'],
                        url = n['url'],
                        timestamp = n['timestamp'],
                        source = n['source'],
                        published = False
                    )
                )
            else:
                logging.info('Newsriver URL {} is a duplicate and already included in DB. Removed from commit stack.'.format(n['url']))
    else:
        logging.info('No newsriver items available to push to database')
    if rss_items is not None:
        logging.info('Pushing RSS items to database')
        for feed_data in rss_items:
            feed_title = feed_data['feed_title']
            for s in feed_data['items']:
                if not is_dupe(item=s, item_type='rss_item'):
                    commit_list.append(
                        RSSEntry(
                            feed_title = feed_title,
                            title = s['title'],
                            url = s['url'],
                            timestamp = s['timestamp'],
                            published = False
                        )
                    )
                else:
                    logging.info('RSS URL {} is a duplicate and already included in DB. Removed from commit stack.'.format(s['url']))

def is_dupe(item, item_type):
    # try rewriting this with args: db_entity, criterium (entry item), target (db data)
    # no more stupid item_type and if-then-monsters.
    if item_type == 'reddit_item':
        return bool(count(e for e in RedditEntry if item['reddit_id'] == e.reddit_id))
    elif item_type == 'newsriver_item':
        return bool(count(e for e in NewsriverEntry if item['url'] == e.url))
    elif item_type == 'rss_item':
        return bool(count(e for e in RSSEntry if item['url'] == e.url))

@db_session
def get_unpublished_db_items():
    reddit_unpub = select(e for e in RedditEntry if e.published == False).order_by(desc(RedditEntry.score))
    newsriver_unpub = select(e for e in NewsriverEntry if e.published == False).order_by(desc(NewsriverEntry.timestamp))
    rss_unpub = select(e for e in RSSEntry if e.published == False).order_by(desc(RSSEntry.timestamp))
    unpub = {
            'reddit': [r for r in reddit_unpub],
            'newsriver': [n for n in newsriver_unpub],
            'rss': [f for f in rss_unpub]
        }
    return unpub

@db_session
def mark_published(unpublished_items=None):
    # pack the ids of unpublished items into a list
    unpub_ids = [i.id for k in unpublished_items for i in unpublished_items[k]]
    for i in unpub_ids:
        Entry[i].published = True
    
@db_session
def get_zen_proverb():
    return Proverb.select_random(1)[0].text     # quick 'n dirty, y'all!