import datetime
from django.db import models
from groups.validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(max_length=80, verbose_name='Group name', db_column='Group')
    groups_start_data = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    group_description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'groups'


