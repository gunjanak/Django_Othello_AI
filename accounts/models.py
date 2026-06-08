from django.contrib.auth.models import AbstractUser
from django.db import models
class OthelloUser(AbstractUser):
    elo = models.IntegerField(default=1200)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    def win_rate(self):
        return 0 if not self.games_played else round(self.wins/self.games_played*100,1)
