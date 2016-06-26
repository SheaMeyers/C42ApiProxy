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
    def test_get_event_title_returns_title_from_response_dict(self, get_event_details_mock):
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