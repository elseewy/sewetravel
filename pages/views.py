from django.shortcuts import render, get_object_or_404,redirect
from .models import Team
from tours.models import Tour
from tourlists.models import TourList
#from letter.forms import SubscibersForm
from . forms import SubscibersForm, MailMessageForm
from . models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = SubscibersForm()

    tourlists = TourList.objects.all()
    tours = Tour.objects.all()
    forms = SubscibersForm()
    top_tours = Tour.objects.order_by("-created_date").filter(is_featured=True)[:4]
    data = {
        'tourlists': tourlists,
        'tours': tours,
        'form': form,
        'top_tours': top_tours,
    }
    return render(request, 'pages/home.html', data)


def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('mail-letter')
    else:
        form = MailMessageForm()
    data = {
        'form': form,
    }
    return render(request, 'pages/mail_chimp.html', data)

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