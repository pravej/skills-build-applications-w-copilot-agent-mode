from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel")
        self.user = User.objects.create(name="Iron Man", email="ironman@marvel.com", team=self.team)
        self.workout = Workout.objects.create(name="Pushups", description="Do 50 pushups", suggested_for="Strength")
        self.activity = Activity.objects.create(user=self.user, type="Running", duration=30, date="2024-01-01")
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_team(self):
        self.assertEqual(self.team.name, "Marvel")

    def test_user(self):
        self.assertEqual(self.user.email, "ironman@marvel.com")

    def test_workout(self):
        self.assertEqual(self.workout.name, "Pushups")

    def test_activity(self):
        self.assertEqual(self.activity.type, "Running")

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 100)
