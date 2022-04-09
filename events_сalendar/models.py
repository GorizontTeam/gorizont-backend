from django.db import models
from accounts.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField('Название', max_length=150)
    date = models.DateTimeField('Дата и время')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name

