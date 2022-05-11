from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name="home"),
    path('signup/',views.registerPage,name="sign-up"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout")
]