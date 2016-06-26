import mock as mock
import os
import django
from django.test import TestCase

from C42ApiProxy.helpers.helpers import get_event_title, get_event_names

# Needed to run unit tests in pycharm
os.environ['DJANGO_SETTINGS_MODULE'] = 'C42ApiProxy.settings'
django.setup()


class GetEventTitleTests(TestCase):

    @mock.patch('C42ApiProxy.helpers.helpers.get_event_details')
    def test_get_event_title_returns_title_from_response_json(self, get_event_details_mock):
        get_event_details_mock.return_value = {u'meta_data':
                                                   {u'count': 1},
                                                    u'data': [
                                                        {u'some-other-key': u'some-other-value',
                                                         u'title': u'Drink a cup of coffee with C42 Team'}
                                                    ]
                                               }
        expected_title = 'Drink a cup of coffee with C42 Team'

        title = get_event_title('fake-event-id')

        self.assertEqual(expected_title, title)

    @mock.patch('C42ApiProxy.helpers.helpers.get_event_details')
    def test_get_event_title_returns_error_message_if_api_call_returns_an_error(self, get_event_details_mock):
        get_event_details_mock.return_value = {u'error':
                                                   {u'status_code': 404,
                                                    u'message': u'Event cc16b1290b812196885e7022956c401d_14667663214311 not found',
                                                    u'code': u'NOT_FOUND'}
                                               }
        expected_title = 'There was an error getting the title'

        title = get_event_title('fake-event-id')

        self.assertEqual(expected_title, title)


class GetEventNamesTests(TestCase):

    @mock.patch('C42ApiProxy.helpers.helpers.get_event_subscriptions')
    def test_get_event_names_returns_names_of_subscribers_from_response_dict(self, get_event_subscriptions_mock):
        get_event_subscriptions_mock.return_value = {
                                                       u'meta_data':{
                                                          u'count':8,
                                                       },
                                                       u'data':[
                                                          {
                                                             u'random-key': u'random-value',
                                                             u'subscriber':{
                                                                u'first_name':u'Name One',
                                                                u'other-key':u'other-value'
                                                             },
                                                          },
                                                          {
                                                             u'random-key': u'random-value',
                                                             u'subscriber':{
                                                                u'first_name':u'Name Two',
                                                                u'other-key':u'other-value'
                                                             },
                                                          },
                                                       ]
                                                    }
        expected_names = ['Name One', 'Name Two']

        names = get_event_names('fake-event-id')

        self.assertEqual(expected_names, names)

    @mock.patch('C42ApiProxy.helpers.helpers.get_event_subscriptions')
    def test_get_event_names_returns_error_message_if_api_call_returns_error(self, get_event_details_mock):
        get_event_details_mock.return_value = {
                                                u'error': {
                                                    u'status_code': 500,
                                                    u'message': u'invalid subscription id given',
                                                    u'code': u'GENERAL_SYSTEM_ERROR'
                                                }
                                            }
        expected_names = ['There was an error getting the names']

        names = get_event_names('fake-event-id')

        self.assertEqual(expected_names, names)