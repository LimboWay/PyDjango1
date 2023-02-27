# Generated by Django 4.1.7 on 2023-02-27 15:55

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
                ('course', models.CharField(choices=[('I', '1 Level'), ('II', '2 Level'), ('III', '3 Level'), ('IV', '4 Level'), ('V', '5 Level'), ('VI', '6 Level')], max_length=30)),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
