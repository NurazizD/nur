from django.shortcuts import render
from .models import Contacts
from django.http import HttpResponse

# Create your views here.
def contact(request):
    if request.method=="POST":
        contact=Contacts()
        ism = request.POST.get('ism')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name=ism
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("<h1>So`rov uchun haxmat</h1>")

    return render(request ,'contact.html')

