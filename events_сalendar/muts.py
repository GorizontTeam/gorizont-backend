import graphene
from django.db.models import Q
from graphene import String, Boolean, Field, List, DateTime, Int, ID

from events_сalendar.models import Event
from events_сalendar.dots import EventDot


class EventCreation(graphene.Mutation):
    class Arguments:
        name = String(required=True)
        start_date = DateTime(required=True)
        finish_date = DateTime(required=False)

    ok = Boolean()
    event = Field(EventDot)
    errors = List(String)

    @staticmethod
    def mutate(root, info, name, start_date, finish_date):
        user = info.context.user
        if user:
            event = Event.objects.create(
                name=name,
                start_date=start_date,
                finish_date=finish_date,
                author=user,
            )
        else:
            return EventCreation(ok=False, errors=['Пользователь не авторизован'])
        return EventCreation(ok=True, event=event)


class Mutation(graphene.ObjectType):
    create_event = EventCreation.Field()
