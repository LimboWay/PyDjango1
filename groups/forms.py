from django import forms
from groups.models import Group
from students.models import Student
# from courses.models import Course


class BaseGroupForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=None, required=False)

    # def save(self, commit=True):
    #     new_group = super().save(commit)
    #     students = self.cleaned_data['students']
    #     for student in students:
    #         student.group = new_group
    #         student.save()

    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


class CreateGroupForm(BaseGroupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.filter(group__isnull=True).select_related('group')

    class Meta(BaseGroupForm.Meta):
        exclude = [
            'headman',
        ]


class UpdateGroupForm(BaseGroupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.all().select_related('group')
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[(student.id, f'{student.first_name} {student.last_name}') for student in
                     self.instance.students.all()],
            label='Headman',
            required=False
        )
        self.fields['headman_field'].choices.insert(0, (0, '-------'))

    class Meta(BaseGroupForm.Meta):
        exclude = [
            'start_date',
            'headman',
        ]
