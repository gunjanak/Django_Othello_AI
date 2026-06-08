import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import GameRecord
from .elo import AI_ELO_BY_DEPTH
@login_required
def profile_view(request):
    user=request.user
    recent=GameRecord.objects.filter(user=user)[:20]
    elo_history=list(reversed([{'date':g.played_at.strftime('%m/%d'),'elo':g.elo_after,'result':g.result} for g in recent]))
    depth_stats={d:{'ai_elo':AI_ELO_BY_DEPTH[d],'games':GameRecord.objects.filter(user=user,ai_depth=d).count(),'wins':GameRecord.objects.filter(user=user,ai_depth=d,result='win').count(),'losses':GameRecord.objects.filter(user=user,ai_depth=d,result='loss').count(),'draws':GameRecord.objects.filter(user=user,ai_depth=d,result='draw').count()} for d in range(1,8)}
    return render(request,'othello_game/profile.html',{'player':user,'recent_games':recent,'elo_history_json':json.dumps(elo_history),'depth_stats':depth_stats})
