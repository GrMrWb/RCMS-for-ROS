from django.urls import path
from UserInterface import views

urlpatterns = [
    path('',views.home, name="home"),
    path('man', views.autotoman, name="home"),
    path('auto', views.mantoauto, name="home"),
    path('instruction/<str:xaxis>/<str:yaxis>',views.instructJSON),
    path('current/<str:xaxis>/<str:yaxis>',views.currentJSON)
]