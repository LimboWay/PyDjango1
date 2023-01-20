import datetime
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker
from students.validators import validate_unique_email, validate_email_domain

DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='first name', validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='last name')
    birthday = models.DateField(default=datetime.date.today)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(validators=[validate_unique_email, validate_email_domain])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_fake_data(cls, count):
        f = Faker()
        for _ in range(count):
            s = cls()
            s.first_name = f.first_name()
            s.last_name = f.last_name()
            s.email = f'{s.first_name}.{s.last_name}@{f.random.choice(DOMAINS)}'
            s.birthday = f.date_between(start_date='-65y', end_date='-18y')
            s.age = f.random_int(min=18, max=65)
            s.save()
