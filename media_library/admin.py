from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from media_library.models import *


# Register your models here.


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created', 'view_count')
    list_filter = ('status', 'view_count',)
    readonly_fields = ('slug', 'view_count',)
    fieldsets = (
        (_('Контент'), {'fields': ('name', 'video_url', 'image',)}),
        (_('Настройки'), {'fields': ('slug', 'status', 'tags', 'topics', 'course')}),
        (_('Статистика'),
         {'fields': ('view_count',)}),
    )
