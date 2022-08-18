from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['user', 'enrollment_date']
    list_per_page = 18
    search_fields = ['user']
