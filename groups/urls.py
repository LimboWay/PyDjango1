from django.urls import path
from groups import views

app_name = 'groups'

urlpatterns = [
    path('', views.GroupListView.as_view(), name='list'),
    path('create/', views.GroupCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.GroupDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.GroupUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.GroupDeleteView.as_view(), name='delete'),

    ]
