import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    img = models.ImageField('Фото', upload_to='user_page_images', height_field=None, width_field=None, max_length=100, null=True, blank=True)
    bio = models.CharField('Информация о себе', max_length=150, null=True, blank=True)
    phone = models.BigIntegerField('Номер телефона', null=True, blank=True)
    city_name = models.CharField('Город', max_length=100, null=True, blank=True)


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email} - {self.username}'

class Token(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "токен авторизации"
