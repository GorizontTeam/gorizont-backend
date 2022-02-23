import graphene
from accounts.dots import Query as BaseQuery

from accounts.muts import Mutation as BaseMutation


class Query(BaseQuery, graphene.ObjectType):
    pass


class Mutation(BaseMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
