from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:id>/', views.task_update, name='task_update'),
    path('delete/<int:id>/', views.task_delete, name='task_delete'),
    path('complete/<int:id>/', views.task_complete, name='task_complete'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
