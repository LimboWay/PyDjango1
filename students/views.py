# from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
# from django.views.decorators.csrf import csrf_exempt
from webargs.fields import Str
from webargs.djangoparser import use_args
from django.db.models import Q
from django.views.generic import UpdateView
from students.forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from students.models import Student
from core.views import CustomUpdateBaseView
# from .utils import format_list_students
# HttpRequest
# HttpResponse
# CRUD - Create Read Update Delete


def get_students(request):
    students = Student.objects.all().order_by('birthday').select_related('group')
    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={
            # 'title': 'List of Students',
            # 'students': students,
            'filter_form': filter_form,
        }
    )


def detail_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'title': 'Detail of student', 'student': student})


def create_student_view(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/create.html', {'form': form})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        form = UpdateStudentForm(instance=student)
    elif request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    return render(request, 'students/update.html', {'form': form})


class CustomUpdateStudentView(CustomUpdateBaseView):
    model = Student
    form_class = UpdateStudentForm
    success_url = 'students:list'
    template_name = 'students/update.html'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


def delete_student(request, pk):
    # st = Student.objects.get(pk=pk)
    st = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': st})
