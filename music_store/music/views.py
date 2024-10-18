from django.shortcuts import render

# Create your views here.

def favorites(request):
    return render(request, "music/favorites.html" )