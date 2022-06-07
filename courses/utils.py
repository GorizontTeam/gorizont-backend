def start_course(course, user):
    if user in course.users_started.all():
        return None
    course.users_started.add(user)
    course.total_started += 1
    course.save()
