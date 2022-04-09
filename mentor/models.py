from django.db import models
from accounts.models import User
from media_library.models import Tag, Topic


# Create your models here.

#
# class Mentor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
#     tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True, related_name='mentors')
#     topics = models.ManyToManyField(Topic, verbose_name='Темы', blank=True, related_name='mentors')
#     description = models.TextField('О себе')
#     free_time = models.CharField('Удобное время для созвонов')
#     communication_contacts = models.TextField('Способы связи')
#
#     class Meta:
#         verbose_name = 'Наставник'
#         verbose_name_plural = 'Наставники'
#
#
# class UserMentor(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
#
