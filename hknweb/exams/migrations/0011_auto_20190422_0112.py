# Generated by Django 2.1.7 on 2019-04-22 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0010_auto_20190421_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='release',
        ),
        migrations.AddField(
            model_name='coursesemester',
            name='release',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
