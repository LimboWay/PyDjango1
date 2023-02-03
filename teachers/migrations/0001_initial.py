# Generated by Django 4.1.6 on 2023-02-02 21:50

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='f_name', max_length=50, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='First name')),
                ('last_name', models.CharField(db_column='l_name', max_length=50, verbose_name='Last name')),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('salary', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
    ]
