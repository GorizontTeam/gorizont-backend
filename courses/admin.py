from django.contrib import admin
from courses.models import *
from django.utils.translation import gettext, gettext_lazy as _


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'total_started', 'total_ended')
    list_filter = ('status', 'is_certificated',)
    readonly_fields = ('total_started', 'total_ended')
    fieldsets = (
        (_('Курс'), {'fields': ('name', 'sort', 'status', 'image', 'short_description', 'description',)}),
        (_('Сертификат'), {'fields': ('is_certificated', 'certificate_text', 'certic_preview_image')}),
        (_('Статистика'),
         {'fields': ('total_started', 'total_ended')}),
        (_('Информация о пользователях'),
         {'fields': ('users_started', 'users_ended', 'users_likes'),
          'classes': ['collapse']}),
    )


# @admin.register(Module)
# class ModuleAdmin(admin.ModelAdmin):
#     list_display = ('name', 'sort', 'course')
#     list_filter = ('course',)
#     fieldsets = (
#         (_('Модуль'), {'fields': ('name', 'sort', 'course',)}),
#         (_('Информация о пользователях'),
#          {'fields': ('users_started', 'users_ended',),
#           'classes': ['collapse']}),
#     )

class TaskFileInline(admin.TabularInline):
    model = TaskFile
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'course', 'is_check_point')
    list_filter = ('is_check_point',)
    fieldsets = (
        (_('Задание'), {'fields': ('name', 'course', 'description', 'video_url')}),
        (_('Настройки'), {'fields': ('sort', 'is_check_point')}),
        (_('Оценка'), {'fields': ('evaluation_criterion', 'points')}),
        (_('Информация о пользователях'),
         {'fields': ('users_started', 'users_ended',),
          'classes': ['collapse']}),
    )
    inlines = [TaskFileInline, ]


# @admin.register(CheckPoint)
# class CheckPointAdmin(admin.ModelAdmin):
#     list_display = ('name', 'course', 'type')
#     list_filter = ('course', 'type')
#     # fieldsets = (
#     #     (_('Задание'), {'fields': ('name', 'description', 'video_url')}),
#     #     (_('Настройки'), {'fields': ('sort', 'module', 'type', 'is_last_task')}),
#     #     (_('Оценка'), {'fields': ('evaluation_criterion', 'points')}),
#     #     (_('Информация о пользователях'),
#     #      {'fields': ('users_started', 'users_ended',),
#     #       'classes': ['collapse']}),
#     # )
