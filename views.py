import db_controller, settings, datetime, time, bots, json, logging

# Slack Attachment Documentation:
# https://api.slack.com/docs/message-attachments


def cap(s, l):
    # caps string length. From here: https://stackoverflow.com/q/11602386
    return s if len(s)<=l else s[0:l-3]+'…'


def format_items(unpublished_items=None):
    msg_format = settings.VIEW_FORMAT or 'terminal'
    zen_proverb = db_controller.get_zen_proverb()
    current_date = datetime.datetime.now().strftime('%A, %d. %B %Y')
    epoch_time = int(time.time())
    structured_rss_items = structure_rss_items(unpublished_items['rss'])
    rendered_items = ''

    for item_type in settings.ITEM_TYPE_ORDER:
        if item_type == 'reddit' and len(unpublished_items['reddit']) > 0:
            rendered_items += '\n\n*Reddit Update ___________________________________________________________________________*\nFrom r/'
            rendered_items += ', r/'.join(settings.SUBREDDIT_LIST)
            rendered_items += '\n\n'
            for r in unpublished_items['reddit']:
                rendered_items += '> [{score}] {title} | {url}\n\n'.format(score=r.score, title=cap(r.title, settings.TITLE_MAX_LENGTH), url=r.url)
            rendered_items += '\n\n\n'
        elif item_type == 'newsriver' and len(unpublished_items['newsriver']) > 0:
            rendered_items += '\n\n*Newsriver Finds _________________________________________________________________________*\n\n'
            for n in unpublished_items['newsriver']:
                rendered_items += '> [{date}: {source}] {title} | {url}\n\n'.format(source=n.source, title=cap(n.title, settings.TITLE_MAX_LENGTH), date=n.timestamp[:10], url=n.url)
            rendered_items += '\n\n\n'
        elif item_type == 'rss' and len(unpublished_items['rss']) > 0:
            rendered_items += '\n\n*Fair Fashion Blogs ______________________________________________________________________*\n\n'
            for feed_title in structured_rss_items:
                rendered_items += '\n\n-------*{ft}* -------\n\n'.format(ft=feed_title)
                for s in structured_rss_items[feed_title]['items']:
                    rendered_items += '> [{date}] {title} | {url}\n\n'.format(title=cap(s.title, settings.TITLE_MAX_LENGTH), date=s.timestamp[:10], url=s.url)
            rendered_items += '\n\n\n'
        elif item_type == 'twitter' and len(unpublished_items['twitter']) > 0:
            rendered_items += '\n\n*Fair Fashion Tweets _____________________________________________________________________*\n\n'
            for t in unpublished_items['twitter']:
                rendered_items += '> [{date}] {title} | Re:({re}) Fav:({fav}) | {url}\n\n'.format(title=t.title, date=str(t.timestamp)[:10], url=t.url, re=t.retweet_count, fav=t.favorite_count)
            rendered_items += '\n\n\n'
        else:
            pass

    if msg_format == 'slack':
        payload = {
            "attachments": [
                {
                    "fallback": 'No plaintext Version available',
                    "color": "#36a64f",
                    "pretext": zen_proverb,
                    "title": 'Kawod Bot News Review {}'.format(current_date),
                    "text": rendered_items,
                    "mrkdwn_in": ["text", "pretext"],
                    "footer": "Kawod Bot v0.1",
                    "ts": epoch_time
                }
            ]
        }
        return json.dumps(payload)
    elif msg_format == 'terminal':
        return rendered_items
    else:
        pass

def publish_items(payload):
    msg_format = settings.VIEW_FORMAT or 'terminal'
    if msg_format == 'slack':
        bots.slack_bot.send_slack_message(payload=payload)
        logging.info('Sent Payload as Incoming Webhook to Slack. Should be displaying shortly.')
    elif msg_format == 'terminal':
        print(payload)
    else:
        pass

def structure_rss_items(rss_items):
    # will return a dict with the structure
    # {FEED_TITLE: {ITEMS: [ENTRY_1, ENTRY_2, ENTRY_X]}}
    structured_rss_items = {}
    for item in rss_items:
        if item.feed_title in structured_rss_items:
            structured_rss_items[item.feed_title]['items'] += [item]
        else:
            structured_rss_items[item.feed_title] = {'items': [item]}
    return structured_rss_items








