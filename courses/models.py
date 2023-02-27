from django.db import models
from groups.models import Group


class Course(models.Model):
    CHOICES = [
        ('I', '1 Level'),
        ('II', '2 Level'),
        ('III', '3 Level'),
        ('IV', '4 Level'),
        ('V', '5 Level'),
        ('VI', '6 Level')
    ]
    course = models.CharField(max_length=30, choices=CHOICES)
    group = models.OneToOneField(Group, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='course_level')

    class Meta:
        db_table = 'courses'
