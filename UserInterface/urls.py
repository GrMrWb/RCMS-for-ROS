from django.urls import path
from UserInterface import views

urlpatterns = [
    path('',views.home, name="home"),
    path('man', views.autotoman, name="home"),
    path('auto', views.mantoauto, name="home")
]