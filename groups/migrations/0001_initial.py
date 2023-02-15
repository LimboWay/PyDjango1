# Generated by Django 4.1.7 on 2023-02-15 15:56

import datetime
from django.db import migrations, models
import groups.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_data', models.DateField(default=datetime.date.today, validators=[groups.validators.validate_start_date])),
                ('group_description', models.CharField(max_length=150)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
    ]
