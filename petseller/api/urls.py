from home.views import *
from django.urls import path

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('animal/<pk>', AnimalDetailsView.as_view()),
    path('register/', RegisterAPI.as_view())

]