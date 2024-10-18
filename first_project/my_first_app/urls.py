from django.urls import path
from . import views

urlpatterns =[
    path('introduction/', views.introduction, name='introduction'),
    path("introduction_bolu/", views.introduction_bolu, name='introduction_bolu')
]