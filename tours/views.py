from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Tour
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from pages.forms import SubscibersForm

# Create your views here.

def tours(request):
    tours = Tour.objects.order_by("created_date")
    forms = SubscibersForm()
    paginator = Paginator(tours, 6)
    page = request.GET.get('page')
    paged_tours = paginator.get_page(page)

    data = {
        'tours': paged_tours,
        'forms': forms,

    }
    return render(request, 'pages/tour-single-list.html', data)


def tour_detail(request, id):
    single_tour = get_object_or_404(Tour, pk=id)
    similar_tours = Tour.objects.order_by("?").filter(is_featured=True)[:3]
    tour_title_search = Tour.objects.values_list('tour_title', flat=True).distinct()
    destination_search = Tour.objects.values_list('destination', flat=True).distinct()
    tours = Tour.objects.all()

    data = {
        'tour_title_search': tour_title_search,
        'destination_search': destination_search,
        'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16],
        'single_tour': single_tour,
        'tours': tours,
        'similar_tours': similar_tours,
    }

    return render(request, 'pages/toursingle.html', data)

def tour_booking(request):
    if request.method == "POST":
        destinations = request.POST['destination']
        datepickers = request.POST['datepicker']
        no_peoples = request.POST['no-people']

        appointment = "Destination: " + destinations + "   Check-In Date: " + datepickers + "  Number People: " + no_peoples
        print(destinations,datepickers,no_peoples)
        send_mail(
            'Booking request', # subject
            appointment,
            'elseewy@gmail.com',
            ['aelsewe@gmail.com'],
            fail_silently=False,

        )
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('home')
    template = 'contact.html'

    return render(request, template)
def search(request):
    tours = Tour.objects.order_by('-created_date')
    tour_title_search = Tour.objects.values_list('tour_title', flat=True).distinct()
    destination_search = Tour.objects.values_list('destination', flat=True).distinct()
    #year_search = Tour.objects.values_list('year', flat=True).distinct()
    #body_style_search = Tour.objects.values_list('body_style', flat=True).distinct()
    #transmission_search = Tour.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tours = tours.filter(description__icontains=keyword)

    if 'tour_title' in request.GET:
        tour_title = request.GET['tour_title']
        if tour_title:
            tours = tours.filter(tour_title__iexact=tour_title)

    if 'destination' in request.GET:
        destination = request.GET['destination']
        if destination:
            tours = tours.filter(destination__iexact=destination)

    #if 'year' in request.GET:
    #   year = request.GET['year']
    #    if year:
    #        cars = cars.filter(year__iexact=year)

    #if 'body_style' in request.GET:
    #    body_style = request.GET['body_style']
    #    if body_style:
    #        cars = cars.filter(body_style__iexact=body_style)


    data = {
        'tours': tours,
        'title_search': title_search,
        'destination_search': destination_search,
    }
    return render(request, 'pages/search.html', data)
