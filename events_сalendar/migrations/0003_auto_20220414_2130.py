# Generated by Django 3.2.9 on 2022-04-14 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events_сalendar', '0002_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events_сalendar.status', verbose_name='Статус'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(verbose_name='Дата и время начала'),
        ),
    ]
