from django.urls import path

from.import views

urlpatterns = [
    path('', views.home , name='home'),
    path('signup',views.handlesignup,name='hanlesignup'),
    path('login',views.handlelogin,name='hanlelogin'),
    path('logout',views.handlelogout,name='hanlelogout'),
]
