# Generated by Django 4.1.2 on 2022-10-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_student_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Attendance',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
