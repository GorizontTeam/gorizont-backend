import graphene
from graphene_django.types import DjangoObjectType
from graphene import Field, String, Int, List, ID
from courses.models import *


class CourseDot(DjangoObjectType):
    class Meta:
        model = Course


class TaskDot(DjangoObjectType):
    class Meta:
        model = Task


class Query(graphene.ObjectType):
    course = Field(CourseDot, id=graphene.ID())
    courses = List(
        CourseDot,
        limit=graphene.Int(),
        offset=graphene.Int()
    )
    task = Field(TaskDot, id=graphene.ID())
    tasks = List(
        TaskDot,
        course_id=graphene.ID(),
        limit=graphene.Int(),
        offset=graphene.Int()
    )

    def resolve_course(self, info, id=None):
        course = Course.objects.filter(id=id).exclude(status='draft').first()
        if course:
            return course
        return None

    def resolve_courses(self, info, limit=None, offset=0):
        qs = Course.objects.all().exclude(status='draft')
        if limit:
            qs = qs[offset:offset + limit]
        return qs

    def resolve_task(self, info, id=None):
        task = Task.objects.filter(id=id).first()
        if task:
            return task
        return None

    def resolve_tasks(self, info, course_id, limit=None, offset=0):
        qs = Task.objects.filter(course__id=course_id)
        if limit:
            qs = qs[offset:offset + limit]
        return qs
