import graphene
from graphene import String, Boolean, Field, List, DateTime, Int, ID

from courses.models import *
from courses.dots import CourseDot
from courses.utils import start_course


class StartCourse(graphene.Mutation):
    class Arguments:
        course_id = ID(required=True)

    ok = Boolean()
    course = Field(CourseDot)
    errors = List(String)

    @staticmethod
    def mutate(root, info, course_id):
        user = info.context.user
        print(user)
        if user:
            course = Course.objects.filter(id=course_id, status='ready').first()
            if course:
                started = start_course(course=course, user=user)
                if started == None:
                    return StartCourse(ok=False, errors=['Пользователь уже начал курс'])
            else:
                return StartCourse(ok=False, errors=['Курс с таким ID не сушествует или еще не открыт для участия'])
        else:
            return StartCourse(ok=False, errors=['Пользователь не авторизован'])
        return StartCourse(ok=True, course=course)


class Mutation(graphene.ObjectType):
    start_course = StartCourse.Field()
