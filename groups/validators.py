import datetime


def validate_start_date(value):
    year = value.year
    month = value.month
    day = value.day
    current_date = datetime.datetime.today()
    if year < current_date.year:
        raise ValueError(f"Your year {year}  is from the past, and the current year is {current_date.year}")
    elif month < current_date.month:
        raise ValueError(f"Your month {month}  is from the past, and the current month is {current_date.month}")
    elif day < current_date.day and month == current_date.month:
        raise ValueError(f"Your day {day}  is from the past, and the current day is {current_date.day}")
