import tweepy, settings, logging, time

# This solution is not going to use Cursors because of a potential memory consumption
# issue. These scripts are goint to be running on an old Raspberry Pi, 
# so memory is an issue. More info here: https://stackoverflow.com/a/23996991

def get_twitter_items(start_id=0)
    api = get_twitter_api()
    query = settings.TW_QUERY
    max_tweets = 1000
    searched_tweets = []
    last_id = -1
    retry_count = 0

    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1))
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            if retry_count > TWITTER_RETRIES:
                break
            logging.error('{}. Retrying in {} seconds. {} more retries.'.format(e, TWITTER_RETRY_SLEEP, TWITTER_RETRIES-retry_count))
            retry_count += 1
            time.sleep(TWITTER_RETRY_SLEEP)

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