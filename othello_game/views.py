import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import GameRecord
from .elo import new_elo, AI_ELO_BY_DEPTH

def game_home(request):
    return render(request,'othello_game/home.html',{'depths':list(AI_ELO_BY_DEPTH.items())})

@login_required
def play_view(request):
    depth=max(1,min(7,int(request.GET.get('depth',5))))
    return render(request,'othello_game/play.html',{
        'depth':depth,'ai_elo':AI_ELO_BY_DEPTH[depth],
        'player_elo':request.user.elo,'depths':list(AI_ELO_BY_DEPTH.items()),
    })

@login_required
@require_POST
def save_game(request):
    try:
        data=json.loads(request.body)
        result=data.get('result')
        if result not in ('win','loss','draw'): return JsonResponse({'error':'Invalid result'},status=400)
        ai_depth=int(data.get('ai_depth',5))
        user=request.user
        elo_before=user.elo
        updated_elo,_=new_elo(elo_before,AI_ELO_BY_DEPTH.get(ai_depth,1100),result)
        GameRecord.objects.create(
            user=user,result=result,ai_depth=ai_depth,
            elo_before=elo_before,elo_after=updated_elo,
            duration_s=int(data.get('duration_s',0)),
            player_score=int(data.get('player_score',0)),
            ai_score=int(data.get('ai_score',0)),
        )
        user.elo=updated_elo; user.games_played+=1
        if result=='win': user.wins+=1
        elif result=='loss': user.losses+=1
        else: user.draws+=1
        user.save()
        return JsonResponse({'status':'ok','elo_before':elo_before,'elo_after':updated_elo,'elo_change':updated_elo-elo_before})
    except Exception as e:
        return JsonResponse({'error':str(e)},status=500)
