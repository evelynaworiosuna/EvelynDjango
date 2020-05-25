from django.shortcuts import render
from django.core.mail import send_mail
from .models import Busines
from .forms import BusinesForm

# Create your views here.

def addlisting(request):
    if request.method == "POST":
        form = BusinesForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'addlisting.html', {})
    else:
        return render(request, 'addlisting.html', {})
        


def listing(request):
    all_business = Busines.objects.all
    return render(request, 'listing.html', {'all':all_business})
    

def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']


        send_mail(
            name,
            email,
            subject,
            ['evelyndirectory@gmail.com'],
        )


                  
        return render(request, 'contact.html', {'name':name })

    else:
        return render(request, 'contact.html', {})

