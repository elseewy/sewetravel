from django.urls import path
from . import views

urlpatterns = [
    path('', views.tours, name='tours'),
    path('<int:id>', views.tour_detail, name='tour_detail'),
]