import praw, settings, logging
from datetime import datetime, timezone


def reddit_login():
    logging.info('Creating Reddit instance')
    try:
        reddit_inst = praw.Reddit(
                # next two args are commented because we only need publicly available infos
                #username = settings.REDDIT_USERNAME,
                #password = settings.REDDIT_PASSWORD,
                client_id = settings.REDDIT_CLIENT,
                client_secret = settings.REDDIT_SECRET,
                user_agent = settings.REDDIT_USER_AGENT
            )
        logging.info('Creation of Reddit instance sucessful')
        return reddit_inst
    except:
        logging.error('Failed to create reddit instance', exc_info=True)

def get_reddit_items():
    reddit_inst = reddit_login()
    reddit_items = []
    for subreddit_name in settings.SUBREDDIT_LIST:
        logging.info('Fetching top posts of subreddit /r/{0}'.format(subreddit_name))
        subreddit = reddit_inst.subreddit(subreddit_name)
        # list comprehension like a normal human being, thanks SO: https://stackoverflow.com/a/2397775
        reddit_items += [
                {
                    'score': subm.score,
                    'title': subm.title, 
                    'author': str(subm.author), 
                    'url': subm.shortlink, 
                    'timestamp': datetime.utcfromtimestamp(subm.created_utc).replace(tzinfo=timezone.utc), 
                    'subreddit': subreddit_name,
                    'reddit_id': subm.id
                } 
                for subm in subreddit.top(time_filter='day', limit=settings.TOP_POSTS_LIMIT)
            ]
    logging.info('Reddit bot finished')
    return reddit_items

