from django.db import models
from accounts.models import User

# Create your models here.
from test_app.models import Test


class Course(models.Model):
    COURSE_STATUSES = (
        ('draft', 'Draft'),
        ('view', 'View'),
        ('ready', 'Ready'),
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField('Название', max_length=200)
    sort = models.PositiveIntegerField('Сортировка')
    short_description = models.CharField('Краткое описание', max_length=175, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='courses/images/%Y/%m/%d/', blank=True, null=True)
    status = models.CharField('Статус', max_length=15, choices=COURSE_STATUSES, default=COURSE_STATUSES[0][0])

    is_certificated = models.BooleanField('Полсе прохождения курса выдается сертификат?')
    certificate_text = models.CharField('Текст на сертификате', max_length=50, blank=True, null=True)
    certic_preview_image = models.ImageField(blank=True, null=True)

    users_started = models.ManyToManyField(User, blank=True, related_name='courses_started')
    users_ended = models.ManyToManyField(User, blank=True, related_name='courses_ended')
    users_likes = models.ManyToManyField(User, blank=True, related_name='courses_liked')

    total_started = models.PositiveIntegerField(default=0, blank=True)
    total_ended = models.PositiveIntegerField(default=0, blank=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


# class Module(models.Model):
#     name = models.CharField('Название', max_length=200)
#     course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE, related_name='modules',
#                                default=None)
#
#     sort = models.PositiveIntegerField('Сортировка')
#
#     users_started = models.ManyToManyField(User, blank=True, related_name='modules_started')
#     users_ended = models.ManyToManyField(User, blank=True, related_name='modules_ended')
#
#     class Meta:
#         ordering = ['sort']
#         verbose_name = 'Модули'
#         verbose_name_plural = 'Модули'
#
#     def __str__(self):
#         return self.name


class Task(models.Model):
    TASK_TYPES = (
        ('Автоматическая проверка', 'Автоматическая проверка'),
        ('Ручная проверка', 'Ручная проверка'),
    )
    name = models.CharField('Название', max_length=200)
    # module = models.ForeignKey(Module, verbose_name='Модуль', on_delete=models.CASCADE)
    description = models.TextField('Описание')
    video_url = models.URLField('Ccылка на видео (если есть видео)')
    type = models.CharField('Тип задания', choices=TASK_TYPES, default=TASK_TYPES[0][0], max_length=23)

    users_started = models.ManyToManyField(User, blank=True, related_name='task_started')
    users_ended = models.ManyToManyField(User, blank=True, related_name='task_ended')

    sort = models.PositiveIntegerField('Сортировка')
    is_last_task = models.BooleanField('Итоговое задание в этом модуле')

    evaluation_criterion = models.TextField('Критерия оценки', default='')
    points = models.PositiveIntegerField('Максимальное кол-во баллов', default=0, blank=True)

    class Meta:
        ordering = ['sort']
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.name


class TaskFile(models.Model):
    task = models.ForeignKey(Task, verbose_name='Задание', on_delete=models.CASCADE)
    file = models.FileField('Файл', upload_to='courses/tasks/files/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Файл задания'
        verbose_name_plural = 'Файлы задания'

    def __str__(self):
        return self.task


class CheckPoint(models.Model):
    СHECK_POINT_TYPES = (
        ('Автоматическая проверка', 'Автоматическая проверка'),
        ('Ручная проверка', 'Ручная проверка'),
    )
    name = models.CharField('Название', max_length=150)
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE)
    type = models.CharField('Тип чек-поинта', choices=СHECK_POINT_TYPES, default=СHECK_POINT_TYPES[0][0], max_length=23)
    task = models.ForeignKey(Task, verbose_name='Задание', on_delete=models.CASCADE, null=True, blank=True)
    test = models.ForeignKey(Test, verbose_name='Тест', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Чек поинт'
        verbose_name_plural = 'Чек поинты'

    def __str__(self):
        return self.name
