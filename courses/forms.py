from django import forms
from courses.models import Course


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CourseCreateForm(CourseBaseForm):
    from groups.models import Group
    groups = forms.ModelChoiceField(queryset=Group.objects.select_related('course'), required=False)

    def save(self, commit=True):
        course = super().save(commit)
        groups = self.cleaned_data['groups']
        for group in groups:
            group.course = course
            group.save()

    class Meta(CourseBaseForm.Meta):
        pass


class CourseUpdateForm(CourseBaseForm):
    pass
