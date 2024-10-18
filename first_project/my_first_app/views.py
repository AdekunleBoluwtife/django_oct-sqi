from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request):
    return HttpResponse("HELLO. My name is Boluwatife")
def introduction(request):
    return HttpResponse("MY NAME ADENIRAN IBRAHIM ADEDEJI")
def introduction_bolu(request):
    return HttpResponse("My name is Adekunle Boluwatife")