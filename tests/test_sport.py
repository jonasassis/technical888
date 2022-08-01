import unittest
import requests
import random
from utils import GetAuthorization


class SportTestCase(unittest.TestCase):
    url = "http://127.0.0.1:5000/sports"
    sport = "FOOTBALL"
    sport_post = {"name": "HORSE RACING", "slug": "HORSE RACING", "active": 1}

    def test_get_sports(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_get_sport_found(self):
        params = "/FOOTBALL"
        resp = requests.get(self.url + params)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 3)

    def test_get_sport_not_found(self):
        params = "/FOOTBALLA"
        resp = requests.get(self.url + params)
        self.assertEqual(resp.status_code, 404)

    def test_post_sport_created(self):
        params = "SPORT" + str(random.randint(1, 1000))
        self.sport_post['name'] = params
        self.sport_post['slug'] = params
        resp = requests.post(self.url + "/" + params, json=self.sport_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json(), self.sport_post)

    def test_post_sport_already_exists_bad_request(self):
        params = "FOOTBALL"
        self.sport_post['name'] = params
        self.sport_post['slug'] = params
        resp = requests.post(self.url + "/" + params, json=self.sport_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 400)

    def test_put_sport_update(self):
        self.sport_post['slug'] = "FOOTBALL" + str(random.randint(1, 1000))
        resp = requests.put(self.url + "/FOOTBALL", json=self.sport_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 200)

    def test_put_sport_no_authorization(self):
        self.sport_post['slug'] = "FOOTBALL" + str(random.randint(1, 1000))
        resp = requests.put(self.url + "/FOOTBALL", json=self.sport_post)
        self.assertEqual(resp.status_code, 500)

    def test_delete_sport_inactivate(self):
        params = "/RUGBY"
        resp = requests.delete(self.url + params, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
