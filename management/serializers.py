from rest_framework import serializers
from .models import Lesson, Student, Teacher, Topic
from core.models import User
from core.serializers import SimpleUserSerializer, UserSerializer


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


class SimpleStudentSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()

    class Meta:
        model = Student
        fields = ["id", "user"]


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return Student.objects.create(user=user, **validated_data)

    class Meta:
        model = Teacher
        fields = '__all__'


class SimpleTeacherSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()

    class Meta:
        model = Teacher
        fields = ["id", "user"]


class TopicSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=True)

    class Meta:
        model = Topic
        fields = '__all__'


class LessonTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['title']


class LessonSerializer(serializers.ModelSerializer):
    topic = LessonTopicSerializer()
    teacher = SimpleTeacherSerializer()
    students = SimpleStudentSerializer(many=True)

    class Meta:
        model = Lesson
        fields = '__all__'
