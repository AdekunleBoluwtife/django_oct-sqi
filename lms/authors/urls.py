from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.all_authors, name="authors")
]