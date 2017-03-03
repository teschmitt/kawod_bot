import os, urllib.parse

# All the auth strings are in environment, so yeah, there's that.
NR_AUTH = os.environ["NR_AUTH"]
NR_QUERY = (
    'title:'
        '(fair* OR fairtrade OR nachhaltig* OR ökosozial* OR öko-sozial* '
        'OR bewusst* OR ethik OR ethisch* OR korrekt* OR ökofair* OR öko-fair* OR '
        'streik*) '
    'AND title:'
        '(kleid* OR mode OR textil* '
        'OR apparel OR shirt OR jeans OR klamotten OR shop*) '
    'AND language:de'
)
NR_QUERY_STRING = 'https://api.newsriver.io/v2/search?limit=15&query=' + urllib.parse.quote(NR_QUERY, safe='')


REDDIT_CLIENT = os.environ["REDDIT_CLIENT"]
REDDIT_SECRET = os.environ["REDDIT_SECRET"]
REDDIT_USERNAME = os.environ["REDDIT_USERNAME"]
REDDIT_PASSWORD = os.environ["REDDIT_PASSWORD"]
REDDIT_USER_AGENT = "kawod bot v0.1"

TWITTER_CONS_KEY = os.environ["TWITTER_CONS_KEY"]
TWITTER_CONS_SECRET = os.environ["TWITTER_CONS_SECRET"]
TWITTER_ACC_TOKEN = os.environ["TWITTER_ACC_TOKEN"]
TWITTER_ACC_SECRET = os.environ["TWITTER_ACC_SECRET"]

LOG_LEVEL = "ERROR"
MARK_PUBLISHED = True

SUBREDDIT_LIST = ['entrepreneur', 'startups']
TOP_POSTS_LIMIT = 5

RSS_LIST = [   
        'http://www.kirstenbrodde.de/?feed=rss2',
        'http://blog.ellenkoehrer.com/feed/',
        'http://www.designmob.de/feed/',
        'https://www.grossvrtig.de/feed/',
        'https://fraujonason.blogspot.com/feeds/posts/default?alt=rss',
        'http://www.modeaffaire.de/feed/',
        'https://www.pinkgreenblog.de/feed/',
    ]

SCRAPE_LIST = [
        'http://beyondfashion.de/'
    ]

DB_TYPE = 'sqlite'
DB_NAME = 'kabot.sqlite'

SLACK_WEBHOOK = os.environ["SLACK_WEBHOOK"]

#options: term, slack, email, html
VIEW_FORMAT = 'slack'
EMAIL_RECIPIENT = ''

ITEM_TYPE_ORDER = ['reddit', 'newsriver']

TITLE_MAX_LENGTH = 100

