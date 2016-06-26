import requests

headers = {'Authorization': 'Token a850fb228b367d3cb2f93814a7f5380ff0583142'}


def get_event_details(event_id):

    url = 'https://demo.calendar42.com/api/v2/events/' + event_id + '/'

    resp = requests.get(url, headers=headers)

    return resp.json()


def get_event_subscriptions(event_id):

    url = 'https://demo.calendar42.com/api/v2/event-subscriptions/?event_ids=[' + event_id + ']'

    resp = requests.get(url, headers=headers)

    return resp.json()
