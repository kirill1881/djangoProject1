from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addtask/', views.add_task),
    path('edittask/', views.edit_task)
]