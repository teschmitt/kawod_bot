import tweepy, settings, logging, time, urllib.parse
from datetime import datetime, timezone
from operator import itemgetter

# This solution is not going to use Cursors because of a potential memory consumption
# issue. These scripts are goint to be running on an old Raspberry Pi, 
# so memory is an issue. More info here: https://stackoverflow.com/a/23996991

def get_twitter_items(since_id):
    api = get_twitter_api()
    last_id = 0
    searched_tweets = []
    retry_count = 0

    while len(searched_tweets) < settings.TWITTER_MAX_TWEETS:
        count = settings.TWITTER_MAX_TWEETS - len(searched_tweets)
        try:
            new_tweets = api.search(
                # q=urllib.parse.quote(settings.TWITTER_QUERY, safe=''),
                q=settings.TWITTER_QUERY, 
                lang=settings.TWITTER_LANG,
                # since_id=str(since_id),
                max_id=str(last_id-1),
                count=count
            )
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            if retry_count > settings.TWITTER_RETRIES:
                logging.error('{}. Permanently failed after {} retries.'.format(e, retry_count))
                break
            logging.error('{}. Retrying in {} seconds. {} more retries.'.format(e, settings.TWITTER_RETRY_SLEEP, settings.TWITTER_RETRIES-retry_count))
            retry_count += 1
            time.sleep(settings.TWITTER_RETRY_SLEEP)
    return format_tweets(tweets=searched_tweets, since_id=since_id)

def format_tweets(tweets, since_id):
    # Passing since_id is ugly, but the Twitter Search API doesn't play nice when max_id *and* since_id are provided,
    # so this is a necessary, temporary workaround.
    # GitHub issue link pending.
    formatted_tweets = [{
            'timestamp': t.created_at.replace(tzinfo=timezone.utc),
            'url': 'https://twitter.com/{user}/status/{status}'.format(
                user=t.user.screen_name,
                status=t.id_str),
            'title': t.text.replace('\n', ' '),       # fuck people who put newlines in their tweets! Fuck 'em!
            'twitter_id': t.id,
            'retweet_count': t.retweet_count,
            'favorite_count': t.favorite_count,
            'twitter_user': t.user.screen_name,
            'twitter_weight': t.retweet_count + t.favorite_count
    } for t in tweets if t.id > since_id]

    if settings.TWITTER_MAX_SAVED_TWEETS > 0:
        return sorted(formatted_tweets, key=itemgetter(settings.TWITTER_SORT_KEY), reverse=True)[:settings.TWITTER_MAX_SAVED_TWEETS]
    else:
        return formatted_tweets

def get_twitter_api():
    # OAthHandler includes too much unused functionality. All we are doing is searching
    # for tweets, so an AppAuthHandler will do. More infos see here:
    # http://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./
    # https://dev.twitter.com/oauth/application-only
    # auth = tweepy.OAuthHandler(settings.TWITTER_CONS_KEY, settings.TWITTER_CONS_SECRET)
    # auth.set_access_token(settings.TWITTER_ACC_TOKEN, settings.TWITTER_ACC_SECRET)
    auth = tweepy.AppAuthHandler(settings.TWITTER_CONS_KEY, settings.TWITTER_CONS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    if (not api):
        logging.error('Failed to authenticate Twitter API')
    else:
        logging.info('Twitter API authentification sucessful! Hooray!')
    return api
