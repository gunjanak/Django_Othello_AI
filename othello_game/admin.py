from django.contrib import admin
from .models import GameRecord
@admin.register(GameRecord)
class GameRecordAdmin(admin.ModelAdmin):
    list_display=('user','result','ai_depth','player_score','ai_score','elo_before','elo_after','played_at')
    list_filter=('result','ai_depth')
    search_fields=('user__username',)
