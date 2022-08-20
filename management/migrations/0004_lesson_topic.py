# Generated by Django 4.1 on 2022-08-20 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0003_teacher_is_engaged_alter_student_gpa"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="management.topic",
            ),
        ),
    ]
