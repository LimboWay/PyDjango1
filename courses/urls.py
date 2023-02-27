from django.urls import path
from courses import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='list'),
    path('create/', views.CourseCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.CourseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CourseDeleteView.as_view(), name='delete'),
]
