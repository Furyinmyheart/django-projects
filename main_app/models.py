from django.db import models

class Work(models.Model):
    organization = models.CharField(verbose_name='Организация', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=16)
    duties = models.TextField(verbose_name='Обязанности')

class Hobby(models.Model):
    hobby_name = models.CharField(verbose_name='Название хобби', max_length=32)
    hobby_desc = models.CharField(verbose_name='Описание хобби', max_length=32, blank=True)

class Study(models.Model):
    place_of_study = models.CharField(verbose_name='Место учёбы', max_length=32)
    discipline = models.CharField(verbose_name='Дисциплина', max_length=32)

