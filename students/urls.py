
from django.urls import path
from students.views import ListStudentView, UpdateStudentView
from students.views import create_student_view

from students.views import detail_student
from students.views import delete_student

app_name = 'students'

urlpatterns = [
    path('', ListStudentView.as_view(), name='list'),
    path('create/', create_student_view, name='create'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('detail/<int:pk>/', detail_student, name='detail'),
    path('delete/<int:pk>/', delete_student, name='delete'),

    ]