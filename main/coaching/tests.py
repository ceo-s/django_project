from django.test import TestCase
from mixer.backend.django import mixer
from .models import *
# Create your tests here.


class CoachingTests(TestCase):
    def setUp(self) -> None:
        self.sport = mixer.blend(SportTag)
        self.train_exp = mixer.blend(TrainingExperience)
        self.coach_exp = mixer.blend(CoachingExperience)
        self.req = mixer.blend(ClientRequest, sport=self.sport, experience=self.train_exp, request="I want pizza")
        self.post = mixer.blend(CoachPosts, sport=self.sport)
        return super().setUp()

    def test_client_request_request(self):
        self.assertEqual(self.req.request, "I want pizza")

    def test_client_request_foreign_keys(self):
        self.assertEqual(self.req.sport, self.sport)
        self.assertEqual(self.req.experience, self.train_exp)


    def test_sport_tag(self):
        self.assertTrue(self.sport)

    def test_coach_posts(self):
        self.assertEqual(self.post.sport, self.sport)

    def test_strs(self):
        self.assertEqual(self.sport.__str__() , self.sport.name)
        self.assertEqual(self.train_exp.__str__() , self.train_exp.description)
        self.assertEqual(self.coach_exp.__str__() , self.coach_exp.description)
        self.assertEqual(self.req.__str__() , str(self.req.pk))
        self.assertEqual(self.post.__str__() , str(self.post.pk))
    