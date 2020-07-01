from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Category,Location

# Create your views here.
def welcome(request):
    return render(request,'gala/welcome.html')

def people (request):
    return render(request,'gala/people.html')
def food (request):
    return render(request,'gala/food.html')    

def travel (request):

    context={
        'images':Image.objects.all()
    }
    return render(request,'gala/travel.html',context)

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images= Image.search_by_category(search_term)

        message = f"{search_term}"


        return render(request, 'gala/search.html',{"message":message,"images":searched_images})


    else:
        message = "You haven't searched for any term"

        return render(request,'gala/search.html',{"message":message})
           
