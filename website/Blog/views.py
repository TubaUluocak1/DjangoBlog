from django.shortcuts import render
from .models import Contact,Slider,Post
from django.views.generic.detail import DetailView

def games(request):
    return render(request,"games.html")

class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"
    slug_field = "slug"

def post(request):
    return render(request,"post.html")

def contact(request):
    if request.method == "POST":
       contact=Contact()
       İsim = request.POST.get('İsim')
       Email = request.POST.get('Email')
       Mesaj = request.POST.get('Mesaj')
       contact.İsim=İsim
       contact.Email=Email
       contact.Mesaj=Mesaj
       contact.save()
    
    return render(request,"contact.html")

def index(request):
    obj = Slider.objects.all()
    context = {
        'obj':obj
    }
    return render(request,"index.html",context)

def pages1(request):
    
   
    return render(request,"pages1.html")

def categories1(request):
    
    return render(request,"categories1.html",{})

