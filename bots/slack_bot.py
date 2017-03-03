import json, requests, settings, logging


def send_slack_message(payload=None):
    webhook_url = settings.SLACK_WEBHOOK
    response = requests.post(webhook_url, data=payload, headers={'Content-Type': 'application/json'})

    if response.status_code != 200:
        raise ValueError('Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))
    else:
        logging.info('Everything turned out much better than we expected!')
        # add published flags to db

