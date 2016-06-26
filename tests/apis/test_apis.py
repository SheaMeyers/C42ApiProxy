import mock as mock
import os
import django
from django.test import TestCase

from C42ApiProxy.apis.apis import get_event_details, get_event_subscriptions

# Needed to run unit tests in pycharm
os.environ['DJANGO_SETTINGS_MODULE'] = 'C42ApiProxy.settings'
django.setup()


class GetEventDetailsTests(TestCase):

    @mock.patch('C42ApiProxy.apis.apis.requests.get')
    def test_get_event_details_makes_get_request_with_correct_parameters(self, requests_get_mock):
        get_event_details('fake-event-id')
        requests_get_mock.assert_called_once_with('https://demo.calendar42.com/api/v2/events/fake-event-id/',
                                         headers={'Authorization': 'Token a850fb228b367d3cb2f93814a7f5380ff0583142'})


class GetEventSubscriptionsTests(TestCase):

    @mock.patch('C42ApiProxy.apis.apis.requests.get')
    def test_get_event_subscriptions_makes_get_request_with_correct_parameters(self, requests_get_mock):
        get_event_subscriptions('fake-event-id')
        requests_get_mock.assert_called_once_with('https://demo.calendar42.com/api/v2/event-subscriptions/?event_ids=[fake-event-id]',
                                                  headers={'Authorization': 'Token a850fb228b367d3cb2f93814a7f5380ff0583142'})