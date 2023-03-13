from django.urls import path
from teachers import views


app_name = 'teachers'

urlpatterns = [
    path('', views.TeacherListView.as_view(), name='list'),
    path('create/', views.TeacherCreateView.as_view(), name='create'),
    # path('detail/<int:pk>/', views.TeacherDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete'),
]
