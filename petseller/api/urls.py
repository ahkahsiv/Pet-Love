from home.views import *
from django.urls import path

urlpatterns = [
    path('animals/', AnimalView.as_view())
]