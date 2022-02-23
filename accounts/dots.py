import graphene
from graphene_django.types import DjangoObjectType
from graphene import Field, String, Int, List, ID
from accounts.models import *


class UserDot(DjangoObjectType):
    phone_number = graphene.String()

    class Meta:
        model = User


class Query(graphene.ObjectType):
    me = Field(UserDot)

    def resolve_me(self, info):
        user = info.context.user
        if user:
            return user
        return None
