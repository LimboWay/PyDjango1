from django.db import models
from groups.models import Group


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Course', db_column='course')

    def __str__(self):
        return f'Group name: {Group.name} == {str(self.name)}'
