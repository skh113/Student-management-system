from rest_framework import serializers
from .models import Student, Teacher
from core.models import User
from core.serializers import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    # need to fix this bug
    def create(self, validated_data):
        user_data = validated_data
        del user_data['gpa']
        print(user_data)
        print(validated_data.get("user"))
        return validated_data

        # user = User.objects.create(**user_data)
        # return Student.objects.create(user=user, **validated_data)
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return Student.objects.create(user=user, **validated_data)

    class Meta:
        model = Teacher
        fields = '__all__'
