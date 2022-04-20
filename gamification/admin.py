from django.contrib import admin
from gamification.models import Achievement

# Register your models here.
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass