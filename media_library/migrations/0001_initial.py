# Generated by Django 3.2.9 on 2022-03-10 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0005_auto_20220310_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=140, unique=True, verbose_name='Слаг')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('text', models.TextField(blank=True, default='<p>Not edited yet.</p>', verbose_name='Текст')),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='media_library/%Y/%m/%d/', width_field='width_field')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='courses.course', verbose_name='Курс')),
                ('tags', models.ManyToManyField(blank=True, related_name='tags_articles', to='media_library.Tag', verbose_name='Тэги')),
                ('topics', models.ManyToManyField(blank=True, related_name='topics_articles', to='media_library.Tag', verbose_name='Темы')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
