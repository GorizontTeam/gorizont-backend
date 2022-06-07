from django.db import models


# Create your models here.

class Test(models.Model):
    name = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.name

class Question(models.Model):
    test = models.ForeignKey(Test, verbose_name='Задание', on_delete=models.CASCADE)
    question_text = models.TextField('Вопрос')
    comment = models.TextField('Комментарие к вопросу')

    class Meta:
        verbose_name = 'Вопрос с одним правильным вариантом ответа'
        verbose_name_plural = 'Вопросы с одним правильным вариантом ответа'

    def __str__(self):
        return self.question_text


class MultiSelectQuestion(models.Model):
    question_text = models.TextField('Вопрос')
    test = models.ForeignKey(Test, verbose_name='Задание', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вопрос с несколькими правильными вариантами ответов'
        verbose_name_plural = 'Вопросы с несколькими правильными вариантами ответов'

    def __str__(self):
        return self.question_text


class AnswerOptions(models.Model):
    answer = models.CharField('Ответ', max_length=300)
    is_right_answer = models.BooleanField('Правильный ответ')
    comment = models.TextField('Комментарие к ответу')

    class Meta:
        verbose_name = 'Варианты ответов'
        verbose_name_plural = 'Варианты ответов'
        abstract = True

    def __str__(self):
        return self.answer


class OneRightAnswerOptions(AnswerOptions):
    question = models.ForeignKey(Question, verbose_name='Вопрос', on_delete=models.CASCADE)


class MultiSelectRightAnswerOptions(AnswerOptions):
    question = models.ForeignKey(MultiSelectQuestion, verbose_name='Вопрос', on_delete=models.CASCADE)
