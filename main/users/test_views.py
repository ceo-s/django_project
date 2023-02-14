from django.test import TestCase
from django.test import Client
from .views import *
from .models import User

class CoachungViewsTest(TestCase):

    def setUp(self) -> None:

        return super().setUp()

    def test_status_code(self):
        resp = self.client.get("/login/")
        resp2 = self.client.get("/logout/")
        resp3 = self.client.get("/register/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp2.status_code, 302)
        self.assertEqual(resp3.status_code, 200)
        #self.assertEqual(resp4.status_code, 200)

    def test_login(self):
        User.objects.create_user(username="alex@mail.ru", email="alex@mail.ru", password="OP692287", type="COACH")
        resp = self.client.get("/form/")
        self.assertEqual(resp.status_code, 302)        
        self.client.login(username="alex@mail.ru", password="OP692287")
        resp2 = self.client.get("/form/")
        self.assertEqual(resp2.status_code, 200)

    def test_cabinet_student(self):
        user = User.objects.create_user(username="alex@mail.ru", email="alex@mail.ru", password="OP692287", type="STUDENT")       
        self.client.login(username="alex@mail.ru", password="OP692287")
        Students.objects.create(pk=user.pk)
        resp = self.client.get(f"/cabinet/{user.pk}/")
        self.assertEqual(resp.status_code, 200)

        

    def test_cabinet_coach(self):
        user1 = User.objects.create_user(username="alex@nail.ru", email="alex@nail.ru", password="OJ692287", type="COACH")
        self.client.login(username="alex@nail.ru", password="OJ692287")
        Coaches.objects.create(pk=user1.pk)
        resp1 = self.client.get(f"/cabinet/{user1.pk}/")
        self.assertEqual(resp1.status_code, 200)