from django.db import models

# Create your models here.


class Achievement(models.Model):
    img = models.ImageField('Файл', upload_to='achievements_images', height_field=None, width_field=None, max_length=100)
    name = models.CharField('Название', max_length=150)
    description = models.CharField('Описание', max_length=100)

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name