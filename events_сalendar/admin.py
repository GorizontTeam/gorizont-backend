from django.contrib import admin
from events_сalendar.models import Event, Status

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass