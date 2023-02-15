from django.db import models
import datetime
from faker import Faker
from groups.validators import validate_start_date


class Group(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    group_description = models.CharField(max_length=150)
    end_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'{self.name} {self.start_data}'

    @classmethod
    def generate_fake_data(cls, count):

        f = Faker()
        lst1 = ['Python', 'Java', 'HTML+CSS', 'C#', 'C/C++', 'DevOPS']
        for _ in range(count):
            gr = cls()
            gr.name = f.random.choice(lst1)
            gr.group_description = f.sentence()
            gr.start_date = f.date_between(start_date='today', end_date='+2y')
            gr.clean_fields()
            gr.save()
