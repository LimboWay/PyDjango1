import datetime
from random import choice

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from core.models import PersonModel
from core.validators import ValidateEmailDomain
from groups.models import Group

VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')


class Student(PersonModel):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')
    phone = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def _generate(cls):
        groups = Group.objects.all()
        student = super()._generate()
        student.group = choice(groups)
        student.save()
