import requests, logging, settings
from datetime import datetime

def get_newsriver_items():
    newsriver_items = []
    logging.info('Fetching Newsriver articles')
    response = requests.get(settings.NR_QUERY_STRING, headers={"Authorization":settings.NR_AUTH})
    newsriver_items = [
            {
                'title': art['title'],
                # Convert string to datetime: https://stackoverflow.com/a/466376
                'timestamp': datetime.strptime(art['discoverDate'], '%Y-%m-%dT%H:%M:%S.%f%z'),
                'url': art['url'],
                'source': art['website']['name']
            }
            for art in response.json()
        ]
    logging.info('Newsriver bot finished')
    return newsriver_items