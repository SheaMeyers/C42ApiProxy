import requests

from C42ApiProxy.settings import API_TOKEN

headers = {'Authorization': 'Token {}'.format(API_TOKEN)}


def get_event_details(event_id):
    """
    Wrapper to make api call to get the event details
    :param event_id: The event id
    :return: The api response as a json object
    """
    url = 'https://demo.calendar42.com/api/v2/events/' + event_id + '/'

    response = requests.get(url, headers=headers)

    return response.json()


def get_event_subscriptions(event_id):
    """
    Wrapper to make api call to get the event subscriptions
    :param event_id: The event id
    :return: The api response as a json object
    """
    url = 'https://demo.calendar42.com/api/v2/event-subscriptions/?event_ids=[' + event_id + ']'

    response = requests.get(url, headers=headers)

    return response.json()
