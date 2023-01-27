from django import forms

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
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

# phone  0-9 () - +    +38 (067) 111-22-33
    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        nums = ''.join(i for i in value if i.isdigit())
        if nums[0] == '8':
            nums = '3' + nums
        if nums[0] == '0':
            nums = '38' + nums
        value = f'+{nums[0]}{nums[1]} ({nums[2:5]}) {nums[5:8]}-{nums[8:10]}-{nums[10:]}'
        return value


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'phone',
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

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        nums = ''.join(i for i in value if i.isdigit())
        if nums[0] == '8':
            nums = '3' + nums
        if nums[0] == '0':
            nums = '38' + nums
        value = f'+{nums[0]}{nums[1]} ({nums[2:5]}) {nums[5:8]}-{nums[8:10]}-{nums[10:]}'
        return value
