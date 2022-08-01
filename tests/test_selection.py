import unittest
import requests
import random
from utils import GetAuthorization


class EventTestCase(unittest.TestCase):
    url = "http://127.0.0.1:5000/selections"
    selection_post = {
                    "name": "X",
                    "event": "Michael x Stace",
                    "price": 7.9,
                    "active": 1,
                    "outcome": "Unsettled"
                }

    def test_get_selections(self):
        resp = requests.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_get_selection_found(self):
        params = "/X/" + self.selection_post['event']
        resp = requests.get(self.url + params)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 5)

    def test_get_selection_not_found(self):
        params = "/AE/" + self.selection_post['event']
        resp = requests.get(self.url + params)
        self.assertEqual(resp.status_code, 404)

    def test_post_selection_created(self):
        params = str(random.randint(1, 20))
        self.selection_post['name'] = params
        params += params + '/' + self.selection_post['event']
        resp = requests.post(self.url + "/" + params, json=self.selection_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 201)

    def test_post_selection_already_exists_bad_request(self):
        params = "X"
        self.selection_post['name'] = params
        params += params + '/' + self.selection_post['event']
        resp = requests.post(self.url + "/" + params, json=self.selection_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 400)

    def test_put_selection_update(self):
        self.selection_post['price'] = str(random.randint(1, 5))
        resp = requests.put(self.url + "/X/Nadal x Rafael", json=self.selection_post, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 201)

    def test_put_selection_no_authorization(self):
        resp = requests.put(self.url + "/X/Nadal x Rafael", json=self.selection_post)
        self.assertEqual(resp.status_code, 500)

    def test_delete_selection_inactivate(self):
        params = "/3/Michael x Stace"
        resp = requests.delete(self.url + params, headers=GetAuthorization().header)
        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()