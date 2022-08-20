from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Lesson, Student, Teacher, Topic
from .serializers import LessonSerializer, StudentSerializer, TeacherSerializer, TopicSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
