from rest_framework import serializers
from .models import Student
from core.serializers import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'user', 'gpa', 'enrollment_date']
