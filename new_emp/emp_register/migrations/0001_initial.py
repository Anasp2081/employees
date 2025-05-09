# Generated by Django 5.1.7 on 2025-03-24 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('emp_code', models.CharField(max_length=3)),
                ('mobile', models.CharField(max_length=10)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_register.position')),
            ],
        ),
    ]
