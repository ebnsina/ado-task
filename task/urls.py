from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('new/', views.new_task, name='new'),
    path('tasks/<int:pk>/', views.task, name='task'),
    path('tasks/<int:pk>/edit', views.edit_task, name='edit'),
    path('tasks/<int:pk>/delete', views.delete_task, name='delete'),
]
