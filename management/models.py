from django.db import models
from django.conf import settings


class Student(models.Model):
    GPA_F = 'F'
    GPA_D = 'D'
    GPA_C = 'C'
    GPA_B = 'B'
    GPA_A = 'A'

    GPA_CHOICES = [
        (GPA_A, 'Excellent'),
        (GPA_B, 'Great'),
        (GPA_C, 'Good'),
        (GPA_D, 'Critical'),
        (GPA_F, 'Fail'),
    ]

    enrollment_date = models.DateField(auto_now=True)
    gpa = models.CharField(
        max_length=1, choices=GPA_CHOICES, default=GPA_C)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Teacher(models.Model):
    joined_date = models.DateField(auto_now=True)
    is_engaged = models.BooleanField(default=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ManyToManyField(Teacher)

    def __str__(self) -> str:
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, null=True)
    class_number = models.PositiveSmallIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    students = models.ManyToManyField(Student)
    start_date = models.DateField()
    finish_date = models.DateField()
