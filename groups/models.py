import datetime

from django.db import models

from core.models import BaseModel
from groups.validators import validate_start_date
from teachers.models import Teacher


class Group(BaseModel):
    name = models.CharField(max_length=50)
    group_description = models.CharField(max_length=150)
    start_date = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    end_date = models.DateField(null=True, blank=True)
    headman = models.OneToOneField(
        'students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group'
    )
    course = models.OneToOneField(
        'courses.Course', on_delete=models.SET_NULL, null=True, blank=True, related_name='course'
    )
    teachers = models.ManyToManyField(to=Teacher, blank=True, related_name='groups')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'Group name: {self.name}'

    @classmethod
    def generate_fake_data(cls):
        for name in 'Python', 'Java', 'HTML+CSS', 'C#', 'C/C++', 'DevOPS', 'PM', 'QA':
            cls.objects.create(name=name)
