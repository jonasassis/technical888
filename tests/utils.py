import requests


class GetAuthorization:

    def __init__(self):
        url = "http://127.0.0.1:5000/login"
        login_post = {"login": "jonas", "password": "1234"}
        resp = requests.post(url, json=login_post)
        self.header = {'Authorization': 'Bearer ' + resp.json()['access_token']}
