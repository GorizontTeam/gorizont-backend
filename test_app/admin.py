from django.contrib import admin
from test_app.models import *

# Register your models here.


class OneRightAnswerOptionsInline(admin.TabularInline):
    model = OneRightAnswerOptions
    extra = 3


class MultiSelectRightAnswerOptionsInline(admin.TabularInline):
    model = MultiSelectRightAnswerOptions
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'test',)
    list_filter = ('test',)
    inlines = (OneRightAnswerOptionsInline,)


@admin.register(MultiSelectQuestion)
class MultiSelectQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'test',)
    list_filter = ('test',)
    inlines = (MultiSelectRightAnswerOptionsInline,)
