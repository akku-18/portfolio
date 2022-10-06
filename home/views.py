from multiprocessing import context
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    context = {'name':'Akshansh', 'project':'portfolio'}
    return render(request, 'home.html', context)

def about(request):
    title = ['Developer', 'Coder', 'Designer']
    description = ['description 1', 'description 2', 'description 3']
    images = ['https://source.unsplash.com/400x200/?developer,html','https://source.unsplash.com/400x200/?coder,css,html','https://source.unsplash.com/400x200/?gamer,designer']
    card = zip(title, description, images)
    context = {'card':card}
    return render(request, 'about.html', context)

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['query']
        phone = request.POST['phone']

        ins = Contact(name=name , email=email, phone=phone, desc=desc)
        ins.save()

    return render(request, 'contact.html')