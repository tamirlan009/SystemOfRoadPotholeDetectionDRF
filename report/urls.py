from django.urls import path
from . import views

urlpatterns = [
    path('get/counttask', views.GetCountTask.as_view()),
]
