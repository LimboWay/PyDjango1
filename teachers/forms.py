from django import forms
import django_filters
from django.forms import ModelForm
from teachers.models import Teacher


class TeachersBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeachersCreateForm(TeachersBaseForm):
    pass


class TeachersUpdateForm(TeachersBaseForm):
    pass


class TeachersFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'birthday': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }
