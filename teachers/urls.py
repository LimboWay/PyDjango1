from django.urls import path, re_path, reverse
from teachers.views import get_teachers
from teachers.views import create_teacher_view
from teachers.views import update_teacher
from teachers.views import detail_teacher
from teachers.views import delete_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),                       # teachers:list      group:list
    path('create/', create_teacher_view, name='create'),       # teachers/create/
    path('update/<int:pk>/', update_teacher, name='update'),
    path('detail/<int:pk>/', detail_teacher, name='detail'),
    path('delete/<int:pk>/', delete_teacher, name='delete'),
]
