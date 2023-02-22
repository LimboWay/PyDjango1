# Generated by Django 4.1.7 on 2023-02-22 23:01

import core.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, validators=[core.validators.ValidateEmailDomain('gmail.com', 'yahoo.com', 'test.com')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(db_column='first_name', max_length=50, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(db_column='last_name', max_length=50, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.PositiveIntegerField(default=10000),
        ),
    ]
