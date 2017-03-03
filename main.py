# -*- coding: utf-8 -*-


import settings, logging, db_controller, views

# Alert the bots!
from bots import reddit_bot, newsriver_bot, slack_bot


# setup the logger
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


if __name__ == '__main__':

    reddit_items = reddit_bot.get_reddit_items()
    newsriver_items = newsriver_bot.get_newsriver_items()

    db_controller.prepare_db()
    db_controller.push_to_db(
            reddit_items=reddit_items, 
            newsriver_items=newsriver_items
        )

    unpublished_items = db_controller.get_unpublished_db_items()

    message = views.format_items(unpublished_items)
    views.publish_items(message)

    mark_read = settings.MARK_PUBLISHED
    if mark_read:
        db_controller.mark_published(unpublished_items)
        logging.info('Published items marked as read')
    else:
        logging.debug('Published items _not_ marked as read')


    # Further workflow:
    # ~~Pull unpublished items from db~~
    # Format text
    # Send msg
    # ~~Mark unpublished items as published~~

