import os, urllib.parse, logging

# All the auth strings are in environment, so yeah, there's that.
NR_AUTH = os.environ["NR_AUTH"]
NR_QUERY = (
    'title:'
        '(fair* OR fairtrade OR nachhaltig* OR ökosozial* OR öko-sozial* '
        'OR bewusst* OR ethik OR ethisch* OR korrekt* OR ökofair* OR öko-fair* OR '
        'streik* OR nachhalt*) '
    'AND title:'
        '(kleid* OR mode OR textil* '
        'OR apparel OR shirt OR jeans OR klamotten OR shop*) '
    'AND language:de'
)
NR_QUERY_STRING = 'https://api.newsriver.io/v2/search?sortBy=discoverDate&sortOrder=DESC&limit=15&query=' + urllib.parse.quote(NR_QUERY, safe='')
NR_RETRIES = 3
NR_RETRY_SLEEP = 10

REDDIT_CLIENT = os.environ["REDDIT_CLIENT"]
REDDIT_SECRET = os.environ["REDDIT_SECRET"]
REDDIT_USERNAME = os.environ["REDDIT_USERNAME"]
REDDIT_PASSWORD = os.environ["REDDIT_PASSWORD"]
REDDIT_USER_AGENT = "kawod bot v0.3 -- See https://github.com/mrgnth/kawod_bot for more information"

TWITTER_CONS_KEY = os.environ["TWITTER_CONS_KEY"]
TWITTER_CONS_SECRET = os.environ["TWITTER_CONS_SECRET"]
TWITTER_ACC_TOKEN = os.environ["TWITTER_ACC_TOKEN"]
TWITTER_ACC_SECRET = os.environ["TWITTER_ACC_SECRET"]
TWITTER_QUERY = (
    '(fair OR faire OR faires OR fairer OR fairtrade OR fair-trade OR '
    '(fair trade) OR sozial OR soziale '
    'OR öko-sozial OR öko-soziale OR öko-faire OR streik OR streikende OR nachhaltig OR '
    'nachhaltige OR nachhaltiger OR nachhaltiges OR sustainable OR slow) '
    '(fashion OR mode OR kleidung OR klamotten OR textil OR textilien OR textilwirtschaft '
    'OR textilprodukte OR textilarbeiterinnen OR textilarbeiter OR textilwirtschaft OR '
    'kleider OR shirt OR shirts)'
)
TWITTER_LANG = 'de'
TWITTER_MAX_TWEETS = 1000
TWITTER_RETRIES = 2
TWITTER_RETRY_SLEEP = 10
TWITTER_MAX_SAVED_TWEETS = 10       # set to 0 to save and publish all
TWITTER_SORT_KEY = 'twitter_weight'

LOG_LEVEL = logging.INFO
MARK_PUBLISHED = True
# MARK_PUBLISHED = False

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
        'http://www.thecoco.org/feed/',
        'http://dariadaria.com/category/fair-fashion/feed',
        'http://www.fashionfika.com/feed/',
        'http://jaeckleundhoesle.de/feed/',
        'https://www.nicetohavemag.de/feed/',
        'http://www.sloris.de/feed/',
        'https://www.noveaux-mag.com/feed/'

    ]

# Web scraping not yet supported!
SCRAPE_LIST = [
        'http://beyondfashion.de/'
    ]

DB_TYPE = 'sqlite'
DB_NAME = 'kabot.sqlite'

SLACK_WEBHOOK = os.environ["SLACK_WEBHOOK"]

#options: term, slack, email, html
VIEW_FORMAT = 'slack'
# VIEW_FORMAT = 'terminal'
EMAIL_RECIPIENT = ''

ITEM_TYPE_ORDER = ['twitter', 'rss', 'newsriver', 'reddit']

TITLE_MAX_LENGTH = 100

SQL_DEBUG = False
