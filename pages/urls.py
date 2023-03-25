from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about, name='about'),
    path('gallery',views.gallery, name='gallery'),
    path('contact',views.contact, name='contact'),
    path('tourlist',views.tourlist, name='tourlist'),
    path('toursinglelist',views.toursinglelist, name='toursinglelist'),
    path('toursingle',views.toursingle, name='toursingle'),
    path('tourbooking', views.tourbooking, name='tourbooking'),
    path('blog',views.blog, name='blog'),
]