import graphene
from graphene_django.types import DjangoObjectType
from graphene import Field, List
from gamification.models import *


class AchievementDot(DjangoObjectType):
    class Meta:
        model = Achievement


class UserAchievementDot(DjangoObjectType):
    class Meta:
        model = UserAchievement


class Query(graphene.ObjectType):
    achievements = graphene.List(AchievementDot)
    achievement = Field(AchievementDot, id=graphene.ID())
    userAchievements = graphene.List(UserAchievementDot)
    userAchievement = Field(UserAchievementDot, achievement_id=graphene.ID())

    def resolve_achievements(self, info):
        achievements = Achievement.objects.all()
        return achievements

    def resolve_achievement(self, info, id):
        achievement = Achievement.objects.get(id=id)
        return achievement

    def resolve_userAchievements(self, info):
        user = info.context.user
        if user:
            return UserAchievement.objects.filter(user=user)
        return None

    def resolve_userAchievement(self, info, achievement_id):
        user = info.context.user
        achievement = Achievement.objects.filter(id=achievement_id).last()
        if user and achievement:
            return UserAchievement.objects.filter(user=user, achievement=achievement).last()
        return None
