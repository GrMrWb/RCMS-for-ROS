from django.urls import path
from UserInterface import views

urlpatterns = [
    path('',views.home, name="home"),
    path('test/',views.testUI),
    path('man', views.autotoman, name="home"),
    path('auto', views.mantoauto, name="home"),
    path('warning/<str:seagull>/<str:tide>', views.warning),
    path('cords/<str:ixaxis>/<str:iyaxis>/<str:cxaxis>/<str:cyaxis>',views.cordOnJSON),
    path('data/<str:procRasPi>/<str:procBoard>/<str:powerRasPi>/<str:powerBoard>',views.infoOnJSON),
]