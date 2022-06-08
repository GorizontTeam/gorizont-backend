from django.contrib import admin
from gamification.models import Achievement, UserAchievement

# Register your models here.
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass

@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    pass