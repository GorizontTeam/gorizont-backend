import graphene
from graphene_django.types import DjangoObjectType
from graphene import Field, List
from gamification.models import *


class AchievementDot(DjangoObjectType):
    class Meta:
        model = Achievement


class Query(graphene.ObjectType):
    achievements = graphene.List(AchievementDot)
    achievement = Field(AchievementDot, id=graphene.ID())

    def resolve_achievements(self, info):
        achievements = Achievement.objects.all()
        return achievements

    def resolve_achievement(self, info, id):
        achievement = Achievement.objects.get(id=id)
        return achievement
