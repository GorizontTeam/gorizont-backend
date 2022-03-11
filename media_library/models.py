from django.db import models
from courses.models import Course


# Create your models here.

class Topic(models.Model):
    name = models.CharField('Название', max_length=150, db_index=True)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class Tag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField('Название', max_length=150, db_index=True)
    slug = models.SlugField('Слаг', max_length=140, blank=True, unique=True)
    video_url = models.URLField('Ссылка на видео', blank=True, null=True)
    text = models.TextField('Текст', blank=True,
                            default='<p>Not edited yet.</p>')  # models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True, related_name='articles')
    topics = models.ManyToManyField(Topic, verbose_name='Темы', blank=True, related_name='articles')
    view_count = models.PositiveIntegerField(default=0, blank=True)
    image = models.ImageField(upload_to='media_library/%Y/%m/%d/',
                              null=True, blank=True, width_field="width_field", height_field="height_field")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE, related_name='articles',
                               default=None)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
