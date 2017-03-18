import tweepy, settings, logging

auth = tweepy.OAuthHandler(settings.TWITTER_CONS_KEY, settings.TWITTER_CONS_SECRET)
auth.set_access_token(settings.TWITTER_ACC_TOKEN, settings.TWITTER_ACC_SECRET)
api = tweepy.API(auth)

