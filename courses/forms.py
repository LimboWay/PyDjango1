from django import forms
from courses.models import Course
# from groups.models import Group


class BaseCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseCreateForm(BaseCourseForm):
    class Meta(BaseCourseForm.Meta):
        pass


class UpdateCreateForm(BaseCourseForm):
    class Meta(BaseCourseForm.Meta):
        exclude = [
            'group',
            ]
