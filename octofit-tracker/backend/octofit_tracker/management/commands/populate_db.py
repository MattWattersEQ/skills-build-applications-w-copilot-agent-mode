from django.core.management.base import BaseCommand
from pymongo import MongoClient, ASCENDING

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[col].drop()

        # Ensure unique index on email for users
        users = db['users']
        users.create_index([('email', ASCENDING)], unique=True)

        # Teams
        teams = [
            {'name': 'Marvel', 'description': 'Marvel superheroes team'},
            {'name': 'DC', 'description': 'DC superheroes team'}
        ]
        db.teams.insert_many(teams)

        # Users (superheroes)
        users_data = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'}
        ]
        db.users.insert_many(users_data)

        # Activities
        activities = [
            {'user': 'Spider-Man', 'activity': 'Web Swinging', 'duration_min': 30},
            {'user': 'Iron Man', 'activity': 'Flight Training', 'duration_min': 45},
            {'user': 'Wonder Woman', 'activity': 'Lasso Practice', 'duration_min': 40},
            {'user': 'Batman', 'activity': 'Martial Arts', 'duration_min': 50}
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {'name': 'Super Strength', 'description': 'Strength training for heroes'},
            {'name': 'Agility Course', 'description': 'Agility and reflexes training'}
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {'user': 'Spider-Man', 'points': 120},
            {'user': 'Iron Man', 'points': 110},
            {'user': 'Wonder Woman', 'points': 130},
            {'user': 'Batman', 'points': 125}
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
