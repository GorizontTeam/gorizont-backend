import graphene
from graphene_django.types import DjangoObjectType
from graphene import Field, List
from events_сalendar.models import *


class EventDot(DjangoObjectType):
    class Meta:
        model = Event


class Query(graphene.ObjectType):
    events = graphene.List(EventDot)
    event = Field(EventDot, id=graphene.ID())

    def resolve_events(self, info):
        events = Event.objects.all()
        return events

    def resolve_event(self, info, id):
        event = Event.objects.get(id=id)
        return event
