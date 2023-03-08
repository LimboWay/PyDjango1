from django.contrib.auth.mixins import LoginRequiredMixin

from teachers.models import Teacher
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from teachers.forms import TeachersCreateForm, TeachersUpdateForm, TeachersFilter
from django.urls import reverse_lazy


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    paginate_by = 10
    context_object_name = "teachers_list"

    def get_filter(self):
        return TeachersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_filter'] = self.get_filter()

        return context


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeachersCreateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeachersUpdateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
