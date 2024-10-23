from django.shortcuts import render

# Create your views here.

def example_dtl(request):
    return render(request, 'dtl/dtl.html' )

def test_dtl(request):
    context = {
        "food": "Rice",
        "ingredients": ['tomatoes','pepper','onions','maggi','salt','groundnut oil'],
        "is_favorite": True,
        "time_to_cook_in_mins": 30
    }
    return render(request, "dtl/test-dtl.html", context)