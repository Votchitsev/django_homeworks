# Generated by Django 3.1.2 on 2021-12-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20211214_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.Teacher'),
        ),
    ]
