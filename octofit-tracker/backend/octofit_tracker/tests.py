from django.test import TestCase
from pymongo import MongoClient

class MongoCollectionsTest(TestCase):
    def setUp(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['octofit_db']

    def test_collections_exist(self):
        collections = self.db.list_collection_names()
        for col in ['users', 'teams', 'activities', 'workouts', 'leaderboard']:
            self.assertIn(col, collections)
