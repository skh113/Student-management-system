from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['user', 'gpa', 'enrollment_date']
    list_per_page = 18
    search_fields = ['user']
    list_editable = ['gpa']


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['user', 'is_engaged', 'joined_date']
    list_per_page = 18
    search_fields = ['user']
    list_editable = ['is_engaged']


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
