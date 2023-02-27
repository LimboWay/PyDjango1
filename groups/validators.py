import datetime
from django.core.exceptions import ValidationError


def validate_start_date(date):
    if date < datetime.date.today():
        raise ValidationError(f'дата старта группы не может быть записана задним числом!')
