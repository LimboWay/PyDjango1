# Generated by Django 4.1.7 on 2023-02-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='course', max_length=50, verbose_name='Course')),
                ('price', models.PositiveIntegerField(default=10000)),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
