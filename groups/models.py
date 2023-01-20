from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=80, verbose_name='Group name', db_column='Group')
    groups_start_data = models.DateField(default='2022-12-06')
    group_description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'groups'

