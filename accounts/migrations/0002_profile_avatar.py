# Generated by Django 4.1.7 on 2023-03-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default.png', null=True, upload_to='avatars/'),
        ),
    ]
