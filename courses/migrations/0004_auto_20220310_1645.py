# Generated by Django 3.2.9 on 2022-03-10 16:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_auto_20220310_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='users_ended',
            field=models.ManyToManyField(blank=True, related_name='task_ended', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_last_task',
            field=models.BooleanField(verbose_name='Итоговое задание в этом модуле'),
        ),
        migrations.AlterField(
            model_name='task',
            name='users_started',
            field=models.ManyToManyField(blank=True, related_name='task_started', to=settings.AUTH_USER_MODEL),
        ),
    ]
