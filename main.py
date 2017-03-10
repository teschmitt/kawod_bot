# -*- coding: utf-8 -*-


import settings, logging, db_controller, views

# Alert the bots!
from bots import reddit_bot, newsriver_bot, rss_bot, slack_bot


# setup the logger
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=settings.LOG_LEVEL)


if __name__ == '__main__':

    reddit_items = reddit_bot.get_reddit_items()
    newsriver_items = newsriver_bot.get_newsriver_items()
    rss_items = rss_bot.get_feed_items()

    db_controller.prepare_db()
    db_controller.push_to_db(
            reddit_items=reddit_items, 
            newsriver_items=newsriver_items,
            rss_items=rss_items
        )

    unpublished_items = db_controller.get_unpublished_db_items()

    message = views.format_items(unpublished_items)
    views.publish_items(message)

    if settings.MARK_PUBLISHED:
        db_controller.mark_published(unpublished_items)
        logging.info('Published items marked as read')
    else:
        logging.debug('Published items _not_ marked as read')


