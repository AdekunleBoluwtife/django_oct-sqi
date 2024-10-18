from django.urls import path

from . import views

urlpatterns=[
    path('', views.homepage, name="homepage"),
    path("book-list/", views.book_list, name="book-list"),
]