from random import randint
from django.db import models
from core.models import PersonModel


class Teacher(PersonModel):
    salary = models.PositiveIntegerField(default=3500)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def _generate(cls):
        teachers = super()._generate()
        teachers.salary = randint(10_000, 100_000)
        teachers.save()