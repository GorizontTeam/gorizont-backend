from gamification.models import *


def create_user_achievement(user_id, achievement_id):
    user = User.objects.filter(id = user_id).last()
    achievement = Achievement.objects.filter(id=achievement_id).last()
    if user and achievement:
        user_achievement = UserAchievement.objects.create(user=user, achievement=achievement)
        return user_achievement