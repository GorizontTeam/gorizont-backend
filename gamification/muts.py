import graphene
from graphene import String, Boolean, Field, List, DateTime, Int, ID

from gamification.dots import UserAchievementDot
from gamification.utils import create_user_achievement


class UserAchievementCreation(graphene.Mutation):
    class Arguments:
        achievement_id = String(required=True)

    ok = Boolean()
    user_achievement = Field(UserAchievementDot)
    errors = List(String)

    @staticmethod
    def mutate(root, info, achievement_id):
        user = info.context.user
        if user:
            user_achievement = create_user_achievement(user.id, achievement_id)
        else:
            return UserAchievementCreation(ok=False, errors=['Пользователь не авторизован'])
        return UserAchievementCreation(ok=True, user_achievement=user_achievement)


class Mutation(graphene.ObjectType):
    create_user_achievement = UserAchievementCreation.Field()
