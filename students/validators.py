from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


DOMAINS = ('gmail.com', 'yahoo.com')


def validate_unique_email(email):
    from students.models import Student
    students = Student.objects.all()
    for st in students:
        if email in st.email:
            raise ValidationError(f'"{email}" - уже занят')


def validate_email_domain(value):
    domain = value.split('@')[-1]
    if domain not in DOMAINS:
        raise ValidationError(f'"{domain}"- не доступен!')


@deconstructible
class ValidateEmailDomain:
    def __init__(self, *domains):
        if domains:
            self.domains = tuple(domains)
        else:
            self.domains = DOMAINS

    def __call__(self, *args, **kwargs):
        domain = args[0].split('@')[-1]
        if domain not in self.domains:
            raise ValidationError(f'"{domain}"- не доступен!.')
