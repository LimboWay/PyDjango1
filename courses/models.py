from django.db import models
from groups.models import Group


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Course', db_column='course')
    price = models.PositiveIntegerField(default=10_000)
    course_group = models.OneToOneField(Group, on_delete=models.SET_NULL,
                                        null=True, blank=True, related_name='group_course')

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f'Course {self.name}'
