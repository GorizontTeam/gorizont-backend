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


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'course')
    list_filter = ('course',)
    fieldsets = (
        (_('Модуль'), {'fields': ('name', 'sort', 'course',)}),
        (_('Информация о пользователях'),
         {'fields': ('users_started', 'users_ended',),
          'classes': ['collapse']}),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort', 'module', 'type')
    list_filter = ('type', 'module', 'is_last_task')
    fieldsets = (
        (_('Задание'), {'fields': ('name', 'description', 'video_url')}),
        (_('Настройки'), {'fields': ('sort', 'module', 'type', 'is_last_task')}),
        (_('Оценка'), {'fields': ('evaluation_criterion', 'points')}),
        (_('Информация о пользователях'),
         {'fields': ('users_started', 'users_ended',),
          'classes': ['collapse']}),
    )


class OneRightAnswerOptionsInline(admin.TabularInline):
    model = OneRightAnswerOptions
    extra = 3


class MultiSelectRightAnswerOptionsInline(admin.TabularInline):
    model = MultiSelectRightAnswerOptions
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'task',)
    list_filter = ('task',)
    inlines = (OneRightAnswerOptionsInline,)


@admin.register(MultiSelectQuestion)
class MultiSelectQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'task',)
    list_filter = ('task',)
    inlines = (MultiSelectRightAnswerOptionsInline,)
