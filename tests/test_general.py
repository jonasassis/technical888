import unittest
import requests
from utils import GetAuthorization


class GeneralTestCase(unittest.TestCase):
    url = "http://127.0.0.1:5000/"
    sport_post = {"name": "CAR RACING", "slug": "CAR RACING", "active": 1}

    event_post = {"name": "Hamilton",
                  "slug": "TENNIS",
                  "active": 1,
                  "type": "preplay",
                  "sport": "CAR RACING",
                  "status": "Pending",
                  "scheduled_start": "2022-08-10 10:00:00"}

    selection_post = {"name": "Win",
                      "event": "Hamilton",
                      "price": 7.9,
                      "active": 1,
                      "outcome": "Unsettled"}

    def test_selections_are_inactive_event_becomes_inactive(self):
        auth = GetAuthorization().header

        # add sport
        params_sport = self.sport_post['name']
        resp_sport = requests.post(self.url + "/sports/" + params_sport, json=self.sport_post, headers=auth)

        # add event
        params_event = self.event_post['name'] + "/" + params_sport
        resp_event = requests.post(self.url + "/events/" + params_event, json=self.event_post, headers=auth)

        # add selection
        params_selection = self.selection_post['name'] + "/" + self.event_post['name']
        resp_selection = requests.post(self.url + "/selections/" + params_selection, json=self.selection_post, headers=auth)

        # selections_are_inactive_event_becomes_inactive
        params_selec_put = self.selection_post['name'] + "/" + self.event_post['name']
        self.selection_post['active'] = 0
        resp_selec_put = requests.delete(self.url + "/selections/" + params_selec_put, json=self.selection_post, headers=auth)

        # get event to check status equals inactive
        resp = requests.get(self.url + "/events/" + params_event)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['active'], 0)
        self.assertEqual(resp_sport.status_code, 201)
        self.assertEqual(resp_event.status_code, 201)
        self.assertEqual(resp_selection.status_code, 201)
        self.assertEqual(resp_selec_put.status_code, 200)