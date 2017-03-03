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
    rendered_items = ''
    if msg_format == 'slack':
        for item_type in settings.ITEM_TYPE_ORDER:
            if item_type == 'reddit':
                rendered_items += '\n\n*Reddit Update ___________________________________________________________________________*\nFrom r/'
                rendered_items += ', r/'.join(settings.SUBREDDIT_LIST)
                rendered_items += '\n\n'
                for r in unpublished_items['reddit']:
                    rendered_items += '- [{score}] {title} r/{sub}: {url}\n\n'.format(score=r.score, title=cap(r.title, settings.TITLE_MAX_LENGTH), sub=r.subreddit, url=r.url)
                rendered_items += '\n\n\n'
            elif item_type == 'newsriver':
                rendered_items += '\n\n*Newsriver Finds _________________________________________________________________________*\n\n'
                for n in unpublished_items['newsriver']:
                    rendered_items += '- [{date}: {source}] {title} - {url}\n\n'.format(source=n.source, title=cap(n.title, settings.TITLE_MAX_LENGTH), date=n.timestamp[:10], url=n.url)
                rendered_items += '\n\n\n'
            else:
                pass

        payload = {
            "attachments": [
                {
                    "fallback": 'PLAINTEXT',
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
    else:
        pass

def publish_items(payload):
    msg_format = settings.VIEW_FORMAT or 'terminal'
    if msg_format == 'slack':
        bots.slack_bot.send_slack_message(payload=payload)
        logging.info('Sent Payload as Incoming Webhook to Slack. Should be displaying shortly.')
    else:
        pass
