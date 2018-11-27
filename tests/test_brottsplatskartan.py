import datetime
import time
import unittest

from unittest.mock import Mock, patch

import brottsplatskartan

BROTTS_URL = "https://brottsplatskartan.se/api"


class TestBrottsplatskartan(unittest.TestCase):

    @staticmethod
    def _get_incident_data():

        datetime_today = datetime.date.today()
        datetime_today_str = str(datetime_today)
        datetime_today_str_full = datetime_today_str + "T10:00:00+0200"
        timedelta = datetime.timedelta(days=1)
        tomorrow = datetime_today + timedelta
        tomorrow_str = str(tomorrow)
        tomorrow_str_full = tomorrow_str + "T10:00:00+0200"

        data = {'data': [{'id': 1234,
                          'pubdate_iso8601': datetime_today_str_full,
                          'title_type': 'Inbrott',
                          'description': 'A description of the crime.'
                          },
                         {'id': 2345,
                          'pubdate_iso8601': tomorrow_str_full,
                          'title_type': 'Brand',
                          'description': 'Another description'
                          }
                         ]
                }
        return data

    def test_no_parameters(self):
        b = brottsplatskartan.BrottsplatsKartan()
        self.assertEqual(b.url, BROTTS_URL + "/events")
        self.assertEqual(b.parameters.get('area'), 'Stockholms län')
        self.assertEqual(b.parameters.get('app'), 'bpk')

    def test_area_parameter(self):
        b = brottsplatskartan.BrottsplatsKartan(
            area="Göteborgs län"
        )
        self.assertEqual(b.parameters.get('area'), 'Göteborgs län')
        self.assertEqual(b.url, BROTTS_URL + "/events")

    def test_long_lat_parameters(self):
        b = brottsplatskartan.BrottsplatsKartan(
            longitude=58.22,
            latitude=10.01,
        )
        self.assertEqual(b.parameters.get('lng'), 58.22)
        self.assertEqual(b.parameters.get('lat'), 10.01)
        self.assertEqual(b.url, BROTTS_URL + "/eventsNearby")

    def test_get_ymd_as_datetime_from_time_strptime(self):

        a_test_date = time.strptime("2018-11-20", "%Y-%m-%d")
        ymd = brottsplatskartan.\
            BrottsplatsKartan._get_datetime_as_ymd(a_test_date)
        self.assertIsInstance(ymd, datetime.datetime)

    @patch('brottsplatskartan.requests.get')
    def test_get_incidents_rate_limited(self, mock_requests):

        mock_requests.return_value = Mock(headers={
            'x-ratelimit-reset': time.time()})
        b = brottsplatskartan.BrottsplatsKartan()
        incidents = b.get_incidents()
        self.assertFalse(incidents)

    @patch('brottsplatskartan.requests.get')
    def test_get_incidents(self, mock_requests):

        data = self._get_incident_data()

        mock_requests.return_value = Mock(headers={'no': 'headers'})
        mock_requests.return_value.json.return_value = data
        b = brottsplatskartan.BrottsplatsKartan()
        incidents = b.get_incidents()
        self.assertEqual(len(incidents), 1)


if __name__ == '__main__':
    unittest.main()
