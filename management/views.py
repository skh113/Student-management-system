from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student, Teacher, Topic
from .serializers import StudentSerializer, TeacherSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
