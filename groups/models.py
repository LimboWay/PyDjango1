from django.db import models
import datetime
from faker import Faker
from groups.validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(max_length=80, verbose_name='Group name', db_column='Group')
    groups_start_data = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    group_description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_name} {self.groups_start_data}'

    @classmethod
    def generate_fake_data(cls, count):
        f = Faker()
        for _ in range(count):
            gr = cls()
            gr.group_name = f.text(max_nb_chars=10)[:-1]
            gr.group_description = f.sentence()
            gr.groups_start_data = f.date_between(start_date='today', end_date='+1y')
            gr.clean_fields()
            gr.save()
