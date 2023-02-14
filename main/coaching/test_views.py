from django.test import TestCase
from django.test import Client
from .views import *

class CoachungViewsTest(TestCase):

    def setUp(self) -> None:

        return super().setUp()

    def test_status_code(self):
        resp = self.client.get("/")
        resp2 = self.client.get("/posts/300/")
        resp3 = self.client.get("/form/")
        resp4 = self.client.get("/requests/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp2.status_code, 302)
        self.assertEqual(resp3.status_code, 302)
        self.assertEqual(resp4.status_code, 200)

    