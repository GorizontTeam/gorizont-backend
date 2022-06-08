# Generated by Django 3.2.9 on 2022-06-07 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20220607_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='task',
            name='video_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ccылка на видео (если есть видео)'),
        ),
    ]
