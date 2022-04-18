from django.db import models
from accounts.models import User


# Create your models here.
class Status(models.Model):
    event_status = models.CharField('Статус события', max_length=150)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.event_status



class Event(models.Model):
    name = models.CharField('Название', max_length=150)
    start_date = models.DateTimeField('Дата и время начала')
    finish_date = models.DateTimeField('Дата и время окончания', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name



