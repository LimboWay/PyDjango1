from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from groups.models import Group
from courses.forms import CourseCreateForm, CourseUpdateForm
from courses.models import Course
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CourseListView(ListView):
    model = Course
    template_name = 'courses/list.html'


class CourseCreateView(CreateView): # LoginRequiredMixin
    model = Course
    form_class = CourseCreateForm
    template_name = 'courses/create.html'
    success_url = reverse_lazy('courses:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        course = form.save()
        groups = form.cleaned_data['groups']
        for group in groups:
            group.course = course
            group.save()
        return response


class CourseDetailView(DetailView):  # LoginRequiredMixin
    model = Course
    template_name = 'courses/detail.html'


class CourseUpdateView(UpdateView):  # LoginRequiredMixin
    model = Course
    template_name = 'courses/update.html'
    # context_object_name = "course"
    form_class = CourseUpdateForm
    success_url = reverse_lazy('courses:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        groups = form.cleaned_data['groups']
        for group in groups:
            group.course = self.object
            if hasattr(group, 'group_course'):
                course = group.course
                course.group = None
                course.save()
            group.save()
        group_pk = int(form.cleaned_data.get('group_field'))
        if group_pk:
            form.instance.group = Group.objects.get(pk=group_pk)
        else:
            form.instance.group = None
        form.save()
        return response


class CourseDeleteView(DeleteView):   # LoginRequiredMixin
    model = Course
    template_name = 'courses/delete.html'
    # context_object_name = "course"
    success_url = reverse_lazy('courses:list')

