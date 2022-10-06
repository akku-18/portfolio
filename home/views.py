from multiprocessing import context
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    context = {'name':'Akshansh', 'project':'portfolio'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['query']
        phone = request.POST['phone']

        ins = Contact(name=name , email=email, phone=phone, desc=desc)
        ins.save()

    return render(request, 'contact.html')