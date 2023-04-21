from django.shortcuts import render, get_object_or_404
from .models import Team
from tours.models import Tour
from tourlists.models import TourList
# Create your views here.

def home(request):

    tourlists = TourList.objects.all()
    tours = Tour.objects.all()
    top_tours = Tour.objects.order_by("-created_date").filter(is_featured=True)[:4]
    data = {
        'tourlists': tourlists,
        'tours': tours,
        'top_tours': top_tours,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def gallery(request):
    return render(request, 'pages/gallery.html')

def contact(request):
    return render(request, 'pages/contact.html')

def blog(request):
    return render(request, 'pages/blog.html')

def tourbooking(request):
    return render(request, 'pages/tourbooking.html')