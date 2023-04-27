from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about, name='about'),
    path('gallery',views.gallery, name='gallery'),
    #path('letter-index/', index, name='letter-index'),
    path('mail_letter/', views.mail_letter, name='mail-letter'),
    path('contact',views.contact, name='contact'),
    path('tourbooking', views.tourbooking, name='tourbooking'),
    path('blog',views.blog, name='blog'),
]