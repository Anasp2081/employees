# Generated by Django 5.1.7 on 2025-03-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='fullname',
            field=models.CharField(max_length=100),
        ),
    ]
