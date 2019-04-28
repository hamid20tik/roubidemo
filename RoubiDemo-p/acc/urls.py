
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.usersignup,name='usersignup'),
    # path('takmil/',views.usert,name='usert'),
]
