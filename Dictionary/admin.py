from django.contrib import admin
from .models import History


# Register your models here.
@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username', 'history', 'query_time')
    ordering = ('userId',)
