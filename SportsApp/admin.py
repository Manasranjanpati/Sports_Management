from django.contrib import admin
from .models import SportsData

class SportsAdmin(admin.ModelAdmin):

    list_display = ['sports_name','sports_type','sports_time','sports_coach']


admin.site.register(SportsData,SportsAdmin)