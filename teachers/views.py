# from django.http import HttpRequest
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from django.views.decorators.csrf import csrf_exempt
from webargs.fields import Str
from webargs.djangoparser import use_args
from django.db.models import Q
from teachers.forms import CreateTeacherForm, UpdateTeacherForm
from teachers.models import Teacher
# from teachers.utils import format_list_teachers
# HttpRequest
# HttpResponse
# CRUD - Create Read Update Delete


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query',
)
def get_teachers(request, args):
    teachers = Teacher.objects.all().order_by('birthday')
    if len(args) and (args.get('first_name') or args.get('last_name')):
        teachers = teachers.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )
    return render(
        request=request,
        template_name='teachers/list.html',
        context={'title': 'List of Teachers', 'teachers': teachers}
    )


def detail_teacher(request, pk):
    # teacher = Teacher.objects.get(pk=pk)
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/detail.html', {'title': 'Detail of Teacher', 'teacher': teacher})


# @csrf_exempt
def create_teacher_view(request):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/create.html', {'form': form})


def update_teacher(request, pk):
    # teacher = Teacher.objects.get(pk=pk)
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/update.html', {'form': form})


def delete_teacher(request, pk):
    # tch = Teacher.objects.get(pk=pk)
    tch = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        tch.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/delete.html', {'teacher': tch})
