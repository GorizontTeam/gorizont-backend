from django.contrib import admin
from events_сalendar.models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass