from django.db import models
from accounts.models import User
from events_сalendar.models import Event

# Create your models here.


class Achievement(models.Model):
    img = models.ImageField('Файл', upload_to='achievements_images', height_field=None, width_field=None,
                            max_length=100)
    name = models.CharField('Название', max_length=150)
    description = models.CharField('Описание', max_length=100)

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name


class UserAchievement(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, verbose_name='Достижение', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Достигнутое достижение'
        verbose_name_plural = 'Достигнутые достиженияя'

    def __str__(self):
        return f'{self.user} - {self.achievement}'


class UserPage(models.Model):
    img = models.ImageField('Фото', upload_to='user_page_images', height_field=None, width_field=None,
                            max_length=100)
    username = models.ForeignKey(User, verbose_name='Имя пользователя', on_delete=models.CASCADE)
    description = models.CharField('Информация о себе', max_length=150)
    achievements_received = models.ForeignKey(UserAchievement, verbose_name="Достигнутые достижения", on_delete=models.CASCADE)
    event_calendar = models.ForeignKey(Event, verbose_name="Календарь событий", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Страница пользователя'
        verbose_name_plural = 'Страницы пользователей'

    def __str__(self):
        return self.username
