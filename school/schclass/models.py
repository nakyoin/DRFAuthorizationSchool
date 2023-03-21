from django.db import models
from rest_framework import serializers

class Journal(models.Model):
    classroom = models.CharField(max_length=100)
    year_of_learning = models.IntegerField(default=None)
    students = models.ManyToManyField('Student', blank=True, related_name='stud')

    class Meta:
        verbose_name = 'Журнал'

    def __str__(self):
        return str(self.classroom)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=None)
    lessons = models.ManyToManyField('Lesson', blank=True, related_name='less')
    grade = models.IntegerField(default=None)


    class Meta:
        verbose_name = 'Ученики'

    def __str__(self):
        return str(self.name)

class Lesson(models.Model):
    lessname = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Предметы'

    def __str__(self):
        return str(self.lessname)