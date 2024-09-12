from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/register/',views.register,name='login/register'),
    path('login/',views.login_user,name='login'),
    path('login/admin',views.admin_user,name='login/admin'),
    path('logout/',views.Logout,name='logout')

]
