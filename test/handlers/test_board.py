from json import loads

import api
from . import APITestCase


class TestBoardHandler(APITestCase):
    url = "/board"

    def test_post(self):
        response = self.post({"BoardId": 100000000})
        body = loads(response.body)
        # assert response.code == 200
        # assert body["Title"] == "Board 100000000"
        # assert len(body["CardTypes"]) == 5
        # assert len(body["ClassesOfService"]) == 4

    def test_ignored(self):
        response = self.post({"BoardId": 100000000})
        body = loads(response.body)
        # assert len(body["CardTypes"]) == 3
        # assert len(body["ClassesOfService"]) == 3

    def test_not_found(self):
        response = self.post({"BoardId": 300000000})
        assert response.code == 404