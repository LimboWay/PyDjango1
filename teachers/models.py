import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='f_name',
                                  validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='l_name')
    birthday = models.DateField(default=datetime.date.today)
    salary = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField()
    city = models.CharField(max_length=25, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        for _ in range(cnt):
            tch = cls()       # tch = Teachers()
            tch.first_name = f.first_name()
            tch.last_name = f.last_name()
            tch.birthday = f.date_between(start_date='-65y', end_date='-18y')
            tch.save()
