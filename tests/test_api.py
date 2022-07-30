import unittest
import requests
import random
import config

sport = "a"
event = "a"


class GetAuthorization:

    def __init__(self):
        url = "http://127.0.0.1:5000/login"
        login_post = {"login": "jonas", "password": "1234"}
        resp = requests.post(url, json=login_post)
        self.header = {'Authorization': 'Bearer ' + resp.json()['access_token']}


class SportTestCase(unittest.TestCase):
    url = "http://127.0.0.1:5000/sports"
    sport = "FOOTBALL"
    sport_post = {"name": "HORSE RACING", "slug": "HORSE RACING", "active": 1}

    def test_get_sports_200(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_get_sport_200(self):
        params = "/FOOTBALL"
        resp = requests.get(self.url + params)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 3)

    def test_post_sport_201(self):
        params = "SPORT" + str(random.randint(1, 1000))
        global sport
        sport = params
        self.sport_post['name'] = params
        self.sport_post['slug'] = params
        resp = requests.post(self.url + "/" + params, json=self.sport_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json(), self.sport_post)

    def test_put_sport_200(self):
        self.sport_post['slug'] = "FOOTBALL" + str(random.randint(1, 1000))
        resp = requests.put(self.url + "/FOOTBALL", json=self.sport_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 200)

    def test_delete_sport_200(self):
        params = "/RUGBY"
        global sport
        print(sport)
        resp = requests.delete(self.url + params, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 200)


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

    def test_get_event_200(self):
        resp = requests.get(self.url)
        global sport
        print(sport)
        self.assertEqual(resp.status_code, 200)

    # def test_get_event_200(self):
    #     global data
    #     params = "/Nadal x Rafael/" + data['sport']
    #     resp = requests.get(self.url + params)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertEqual(len(resp.json()), 8)
    #
    # def test_post_event_201(self):
    #     global data
    #     params = "EVENT" + str(random.randint(1, 1000))
    #     data['event'] = params
    #     self.event_post['name'] = params
    #     self.event_post['slug'] = params
    #     params += params + '/' + data['sport']
    #     resp = requests.post(self.url + "/" + params, json=self.event_post, headers=GetAuthorization().header)
    #     self.assertEqual(resp.status_code, 201)
    #     self.assertEqual(resp.json(), self.event_post)
    #
    # def test_put_event_200(self):
    #     self.event_post['slug'] = "Nadal x Rafael " + str(random.randint(1, 1000))
    #     resp = requests.put(self.url + "/Nadal x Rafael/TENNIS", json=self.event_post, headers=GetAuthorization().header)
    #     self.assertEqual(resp.status_code, 200)
    #
    # def test_delete_event_200(self):
    #     params = "/Nadal x Rafael/TENNIS"
    #     resp = requests.delete(self.url + params, headers=GetAuthorization().header)
    #     self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
