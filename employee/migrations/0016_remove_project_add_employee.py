# Generated by Django 4.2.1 on 2023-08-18 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_employee_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='add_employee',
        ),
    ]