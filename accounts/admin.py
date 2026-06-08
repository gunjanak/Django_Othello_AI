from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import OthelloUser
@admin.register(OthelloUser)
class OthelloUserAdmin(UserAdmin):
    list_display = ('username','email','elo','wins','losses','draws','games_played')
    fieldsets = UserAdmin.fieldsets+(('Othello Stats',{'fields':('elo','wins','losses','draws','games_played')}),)
