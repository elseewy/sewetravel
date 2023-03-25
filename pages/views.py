from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def contact(request):
    return render(request, 'pages/contact.html')

def tourlist(request):
    return render(request, 'pages/tourlist.html')

def toursinglelist(request):
    return render(request, 'pages/tour-single-list.html')

def toursingle(request):
    return render(request, 'pages/toursingle.html')

def blog(request):
    return render(request, 'pages/blog.html')

def tourbooking(request):
    return render(request, 'pages/tourbooking.html')