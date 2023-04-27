from django.urls import path
from . import views
#from letter.views import index,mail_letter

urlpatterns = [
    path('', views.tours, name='tours'),
    path('<int:id>', views.tour_detail, name='tour_detail'),
    #path('letter-index/', index, name='letter-index'),
    #path('mail_letter/', mail_letter, name='mail-letter'),
    path('contact/', views.tour_booking, name='contact'),
    path('search', views.search, name='search'),
]