from django.db import models
from django.conf import settings
class GameRecord(models.Model):
    RESULTS = [('win','Win'),('loss','Loss'),('draw','Draw')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='games')
    result = models.CharField(max_length=10, choices=RESULTS)
    ai_depth = models.IntegerField()
    elo_before = models.IntegerField()
    elo_after = models.IntegerField()
    played_at = models.DateTimeField(auto_now_add=True)
    duration_s = models.IntegerField(default=0)
    player_score = models.IntegerField(default=0)
    ai_score = models.IntegerField(default=0)
    class Meta: ordering=['-played_at']
    def elo_change(self): return self.elo_after - self.elo_before
    def duration_display(self):
        m,s=divmod(self.duration_s,60); return f"{m}m {s}s"
