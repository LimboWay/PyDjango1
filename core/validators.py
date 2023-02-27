from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

import re

DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')


def validate_email_domain(value):
    domain = value.split('@')[-1]
    if domain not in DOMAINS:
        raise ValidationError(f'Emails domain "{domain}" is not correct.')


def validate_email_unique(value):
    from students.models import Student
    db_email = Student.objects.values('email')
    filter_emails = []
    for items in db_email:
        emails = items.values()
        for email in emails:
            filter_emails.append(email)
    if value in filter_emails:
        raise ValidationError(f'Email address <{value}> is busy please try another one')


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
            raise ValidationError(f'Emails domain "{domain}" is invalid.')
