import unittest
import requests
import random
from utils import GetAuthorization


class EventTestCase(unittest.TestCase):
    url = "http://127.0.0.1:5000/events"
    event_post = {
                    "name": "Nadal x Rafael",
                    "slug": "TENNIS",
                    "active": 1,
                    "type": "preplay",
                    "sport": "TENNIS",
                    "status": "Pending",
                    "scheduled_start": "2022-08-30 20:00:00"
                }

    def test_get_events(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_get_event_found(self):
        params = "/Nadal x Rafael/" + self.event_post['sport']
        resp = requests.get(self.url + params)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 8)

    def test_get_event_not_found(self):
        params = "/A x Rafael/" + self.event_post['sport']
        resp = requests.get(self.url + params)
        self.assertEqual(resp.status_code, 404)

    def test_post_event_created(self):
        params = "Nadal x Rafael" + str(random.randint(1, 1000))
        self.event_post['name'] = params
        self.event_post['slug'] = params
        params += params + '/' + self.event_post['sport']
        resp = requests.post(self.url + "/" + params, json=self.event_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 201)

    def test_post_event_already_exists_bad_request(self):
        params = "Nadal x Rafael"
        self.event_post['name'] = params
        self.event_post['slug'] = params
        params += params + '/' + self.event_post['sport']
        resp = requests.post(self.url + "/" + params, json=self.event_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 400)

    def test_put_event_update(self):
        self.event_post['slug'] = "Nadal x Rafael " + str(random.randint(1, 1000))
        resp = requests.put(self.url + "/Nadal x Rafael/TENNIS", json=self.event_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 200)

    def test_put_event_no_authorization(self):
        resp = requests.put(self.url + "/Nadal x Rafael/TENNIS", json=self.event_post)
        self.assertEqual(resp.status_code, 401)

    def test_delete_event_inactivate(self):
        params = "/Nadal x Rafael/TENNIS"
        resp = requests.delete(self.url + params, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()