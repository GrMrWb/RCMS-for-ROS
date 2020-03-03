from django.urls import path
from UserInterface import views

urlpatterns = [
    path('',views.home, name="home"),
    path('auto', views.autotoman, name="home"),
    path('man', views.mantoauto, name="home")
]