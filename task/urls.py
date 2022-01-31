from django.urls import path
from task.views import *

urlpatterns = [
    path("" , task_view , name = "task"),
]