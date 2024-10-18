from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "library/home.html")

def book_list(request):
    return render(request,"library/booklist.html")