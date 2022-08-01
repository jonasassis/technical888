import unittest
import requests
import random
from utils import GetAuthorization


class DisplayTestCase(unittest.TestCase):
    url = "http://127.0.0.1:5000/"

    def test_get_display(self):
        url = "display"
        resp = requests.get(self.url + url)
        self.assertEqual(resp.status_code, 200)

    def test_get_events_sport(self):
        url = "events/sport"
        resp = requests.get(self.url + url)
        self.assertEqual(resp.status_code, 200)

    def test_get_events_min(self):
        url = "eventsmin"
        resp = requests.get(self.url + url)
        self.assertEqual(resp.status_code, 200)

    def test_get_sports_min(self):
        url = "sportsmin"
        resp = requests.get(self.url + url)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
