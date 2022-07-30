import unittest
import requests
import random

data = dict()


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

    def test_get_sports(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_get_sport(self):
        params = "/FOOTBALL"
        resp = requests.get(self.url + params)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 3)

    def test_post_sport(self):
        params = "TESTE" + str(random.randint(1, 1000))
        data['sport'] = params
        self.sport_post['name'] = params
        self.sport_post['slug'] = params
        resp = requests.post(self.url + "/" + params, json=self.sport_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json(), self.sport_post)

    def test_put_sport(self):
        self.sport_post['slug'] = "FOOTBALL" + str(random.randint(1, 1000))
        resp = requests.put(self.url + "/FOOTBALL", json=self.sport_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 200)

    def test_delete_sport(self):
        params = "/RUGBY"
        resp = requests.delete(self.url + params, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
