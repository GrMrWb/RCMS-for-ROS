from django.urls import path
from UserInterface import views

urlpatterns = [
    # path('',views.home, name="home"),
    path('',views.testUI),
    path('man', views.testUIman, name="test"),
    path('auto', views.testUIauto, name="test"),
    # path('man', views.autotoman, name="home"),
    # path('auto', views.mantoauto, name="home"),
    # path('automation/',views.automation),
    path('warning/<str:seagull>/<str:tide>', views.warning),
    path('cordsFromRos/<str:currentPosition>', views.cordsFromRos),
    path('cords/<str:ixaxis>/<str:iyaxis>/<str:cxaxis>/<str:cyaxis>',views.cordOnJSON),
    path('data/<str:processedData>',views.infoOnJSON),
]