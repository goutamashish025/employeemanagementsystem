# Generated by Django 4.2.1 on 2023-08-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_alter_project_add_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=25),
        ),
    ]
