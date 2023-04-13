from django.urls import path
from . import views

urlpatterns = [
    path('', views.tourlists, name='tourlists'),
]