from django.db import models
from accounts.models import User


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


class AchievementUser(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    achivement = models.ForeignKey(Achievement, verbose_name='Достижение', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Достигнутое достижение'
        verbose_name_plural = 'Достигнутые достиженияя'

    def __str__(self):
        return self.user
