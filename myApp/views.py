from django.shortcuts import render,get_object_or_404
from myApp.models import *
from django.db.models import Q

# Create your views here.
def index(request):
    post = Yeni.objects.all().order_by("-date")

    # Search Bölümü Kodlaması
    search = request.GET.get("q")
    if search:
        post = post.filter(Q(title__icontains = search) |
                           Q(feature__icontains = search))

    context = {
        'post':post,
    }
    return render(request,"index.html",context)

def detail(request,title):
    post = get_object_or_404(Yeni,title=title)
    context = {
        'post':post,
    }
    return render(request,"detail.html",context)

def signin(request):
    
    return render(request , "signin.html",)