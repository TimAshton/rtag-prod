from django.contrib import admin
from .models import Challenge, Rtag, Scoreboard, User


# Register your models here.
admin.site.register([Challenge, Rtag, Scoreboard, User])
# @admin.register(Rtag)

# class ChallengeAdmin(admin.ModelAdmin):
#     list_display = ['title','description','created_date','status']

# class RtagAdmin(admin.ModelAdmin):
#     list_display = ['owner_id','title','longitude','latitude','elevation']
