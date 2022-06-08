import graphene
from accounts.dots import Query as BaseQuery
from events_сalendar.dots import Query as EventQuery
from gamification.dots import Query as AchievementQuery
from courses.dots import Query as CoursesQuery

from accounts.muts import Mutation as BaseMutation
from events_сalendar.muts import Mutation as EventsMutation
from gamification.muts import Mutation as GamificationMutation
from courses.muts import Mutation as CoursesMutation


class Query(BaseQuery, EventQuery, AchievementQuery, CoursesQuery, graphene.ObjectType):
    pass


class Mutation(BaseMutation, EventsMutation, GamificationMutation, CoursesMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
