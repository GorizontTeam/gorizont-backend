import graphene
from accounts.dots import Query as BaseQuery
from events_сalendar.dots import Query as EventQuery

from accounts.muts import Mutation as BaseMutation
from events_сalendar.muts import Mutation as EventsMutation


class Query(BaseQuery, EventQuery, graphene.ObjectType):
    pass


class Mutation(BaseMutation, EventsMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
