# Generated by Django 4.1.7 on 2023-02-27 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
    ]
