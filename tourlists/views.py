from django.shortcuts import render


# Create your views here.

def tourlists(request):
    return render(request, 'pages/tourlist.html')