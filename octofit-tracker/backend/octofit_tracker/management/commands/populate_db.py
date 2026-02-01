from django.core.management.base import BaseCommand

from octofit_tracker.models import User, Team, Workout, Activity, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Drop collections directly to avoid unhashable errors
        db = connection.cursor().db_conn.client[connection.settings_dict['NAME']]
        db.activity.drop()
        db.leaderboard.drop()
        db.user.drop()
        db.workout.drop()
        db.team.drop()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Web Swing', description='Swinging through the city', difficulty='Medium'),
            Workout.objects.create(name='Flight', description='Flying workout', difficulty='Hard'),
            Workout.objects.create(name='Strength', description='Super strength training', difficulty='Hard'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], workout=workouts[0], duration_minutes=30, calories_burned=200)
        Activity.objects.create(user=users[1], workout=workouts[1], duration_minutes=45, calories_burned=350)
        Activity.objects.create(user=users[2], workout=workouts[2], duration_minutes=60, calories_burned=400)
        Activity.objects.create(user=users[3], workout=workouts[1], duration_minutes=50, calories_burned=300)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=550)
        Leaderboard.objects.create(team=dc, total_points=700)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
