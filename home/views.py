from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from .models import Contact, Skill, Reference
from django.contrib import messages

# Create your views here.
def index(request):
    data = {
        'skills': Skill.objects.all(),
        'references': Reference.objects.all()
    }
    return render(request, 'index.html',data)

def contact(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        date = datetime.today()
        contact = Contact(name=name,email=email,subject=subject,message=message,date=date)
        contact.save()
        messages.success(request, "Message has been sent successfully")
    return redirect('/')