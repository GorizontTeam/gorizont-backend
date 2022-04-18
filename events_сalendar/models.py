from django.db import models
from accounts.models import User


# Create your models here.
class Event(models.Model):
    STATUSES = (
        ('В ожидании', 'В ожидании'),
        ('Активен', 'Активен'),
        ('Закончен', 'Закончен'),
    )
    name = models.CharField('Название', max_length=150)
    start_date = models.DateTimeField('Дата и время начала')
    finish_date = models.DateTimeField('Дата и время окончания', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    status = models.CharField('Статус', max_length=10, choices=STATUSES, default='В ожидании')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name



