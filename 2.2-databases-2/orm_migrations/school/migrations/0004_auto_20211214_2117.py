# Generated by Django 3.1.2 on 2021-12-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20211214_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.Teacher'),
        ),
    ]
