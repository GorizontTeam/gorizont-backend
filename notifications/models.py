from django.db import models
from accounts.models import User


# Create your models here.

class UserNotification(models.Model):
    NOTIFICATION_TYPE = (
        ('встреча', 'Встреча'),
        ('дедлайн задания', 'Дедланй задания'),
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField('Название', max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Описание')
    type = models.CharField('Тип', choices=NOTIFICATION_TYPE, default=NOTIFICATION_TYPE[0][0], max_length=15)

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    def __str__(self):
        return self.name


class NotificationMailing(models.Model):
    NOTIFICATION_TYPE = (
        ('встреча', 'Встреча'),
        ('дедлайн задания', 'Дедланй задания'),
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField('Название', max_length=150)
    date_time = models.DateTimeField('Дата и время отправки')
    send_to_all_users = models.BooleanField('Отправить всем пользователям')
    users = models.ManyToManyField(User)
    text = models.TextField('Описание')
    type = models.CharField('Тип', choices=NOTIFICATION_TYPE, default=NOTIFICATION_TYPE[0][0], max_length=15)

    class Meta:
        verbose_name = 'Рассылка уведомления'
        verbose_name_plural = 'Рассылка уведомления'

    def __str__(self):
        return self.name
