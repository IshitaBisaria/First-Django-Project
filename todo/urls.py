from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path("", views.index, name="home"),
    path("task-list", views.task_list, name="task-list"),
    path("add-task", views.add_task, name="add-task"),
    # path("task/<int:task_id>", views.task, name="task-detail"),
]
