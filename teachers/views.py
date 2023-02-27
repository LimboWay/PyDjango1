from django.contrib.auth.mixins import LoginRequiredMixin

from teachers.models import Teacher
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from teachers.form import CreateTeacherForm, UpdateTeacherForm
from django.urls import reverse_lazy


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    paginate_by = 10
    context_object_name = "teachers_list"


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teachers/create.html'
    form_class = CreateTeacherForm
    success_url = reverse_lazy("teachers:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TeacherDetailView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher_detail'


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    queryset = Teacher.objects.all()
    template_name = 'teachers/update.html'
    context_object_name = 'teacher_update'
    form_class = UpdateTeacherForm
    success_url = reverse_lazy('teachers:list')


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    queryset = Teacher.objects.all()
    template_name = 'teachers/delete.html'
    context_object_name = 'teacher_delete'
    success_url = reverse_lazy('teachers:list')
