from django.db import models
from django.conf import settings


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    enrollment_date = models.DateField(auto_now=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ManyToManyField(Teacher)


class lesson(models.Model):
    title = models.CharField(max_length=255)
    class_number = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    students = models.ManyToManyField(Student)
