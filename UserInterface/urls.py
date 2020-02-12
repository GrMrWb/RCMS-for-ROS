from django.urls import path
from UserInterface import views

urlpatterns = [
    path('',views.home, name="home")
]