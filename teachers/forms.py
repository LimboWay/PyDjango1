from django import forms
from django_filters import FilterSet
from teachers.models import Teacher


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'salary',
            'email',
            'city',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        return value.capitalize()


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'salary',
            'email',
            'city',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        return value.capitalize()


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['exact', 'icontains'],           # first_name = 'Alex',   first_name ILIKE '%abc%'
            'last_name': ['exact', 'startswith']              # last_name LIKE 'ABC%'
        }       # AND (OR)
