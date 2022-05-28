# Generated by Django 3.2.9 on 2022-05-28 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='img',
            field=models.ImageField(upload_to='achievements_images', verbose_name='Файл'),
        ),
        migrations.CreateModel(
            name='AchievementUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achivement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamification.achievement', verbose_name='Достижение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Достигнутое достижение',
                'verbose_name_plural': 'Достигнутые достиженияя',
            },
        ),
    ]