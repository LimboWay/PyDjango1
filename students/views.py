from django.shortcuts import render, get_object_or_404
from students.forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from students.models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from copy import copy


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'
    paginate_by = 12

    def get_filter(self):
        students = Student.objects.all().order_by('birthday').select_related('group', 'headman_group')
        filter_form = StudentFilterForm(data=self.request.GET, queryset=students)
        return filter_form

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_filter().form

        return context


@login_required
def detail_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(
        request=request,
        template_name="students/detail.html",
        context={
            'student': student,
            'title': 'Detail of student'

        }
    )


# @csrf_exempt
@login_required
def create_student_view(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == "POST":
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/create.html',
        context={
            "form": form,
        }

    )


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


@login_required
def delete_student(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/delete.html',
        context={
            'student': student,

        }
    )
