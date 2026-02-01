from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Web Swing', description='Swinging through the city', difficulty='Medium')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration_minutes=30, calories_burned=200)
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Web Swing')

    def test_activity_creation(self):
        self.assertEqual(self.activity.user, self.user)
        self.assertEqual(self.activity.workout, self.workout)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.team, self.team)
        self.assertEqual(self.leaderboard.total_points, 100)
