from django.contrib import admin
from notifications.models import *


# Register your models here.

#
# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'status', 'total_started', 'total_ended')
#     list_filter = ('status', 'is_certificated',)
#     readonly_fields = ('total_started', 'total_ended')
#     fieldsets = (
#         (_('Курс'), {'fields': ('name', 'sort', 'status', 'image', 'short_description', 'description',)}),
#         (_('Сертификат'), {'fields': ('is_certificated', 'certificate_text', 'certic_preview_image')}),
#         (_('Статистика'),
#          {'fields': ('total_started', 'total_ended')}),
#         (_('Информация о пользователях'),
#          {'fields': ('users_started', 'users_ended', 'users_likes'),
#           'classes': ['collapse']}),
#     )


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'user', 'created')
    list_filter = ('type', 'created')

@admin.register(NotificationMailing)
class NotificationMailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created')
    list_filter = ('type', 'created')