from django.urls import path
from students.views import get_students
from students.views import create_student_view
# from .views import update_student
from students.views import detail_student
from students.views import delete_student
# from .views import CustomUpdateStudentView
from students.views import UpdateStudentView

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),                       # students:list      group:list
    path('create/', create_student_view, name='create'),       # students/create/
    # path('update/<int:pk>/', update_student, name='update'),
    # path('update/<int:pk>/', CustomUpdateStudentView.update, name='update'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('detail/<int:pk>/', detail_student, name='detail'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
