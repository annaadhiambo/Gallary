from django.shortcuts import render
from django.http  import HttpResponse 
from .models import Image
# Create your views here.
def home(request):
    images = Image.objects.all()
    context = {
        'images':images
    }
    return render(request, 'home.html',context)
    
def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"

        context = {
            'images':searched_photos,
            'message':message,
        }

        return render(request, 'photo/search.html',context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'photo/search.html',{"message":message})

