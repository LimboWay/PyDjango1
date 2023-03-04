from django.contrib.auth.mixins import LoginRequiredMixin
from courses.forms import CourseCreateForm, UpdateCreateForm
from courses.models import Course
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


class CourseListView(ListView):
    model = Course
    template_name = 'courses/list.html'
    context_object_name = "courses"


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'courses/create.html'
    context_object_name = "courses"
    success_url = reverse_lazy('courses:list')


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = "course"


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = 'courses/update.html'
    context_object_name = "course"
    form_class = UpdateCreateForm
    success_url = reverse_lazy('courses:list')


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'courses/delete.html'
    context_object_name = "course"
    success_url = reverse_lazy('courses:list')
