from django.urls import path,include
from . import views

urlpatterns = [
    path('login',views.make_login, name = "login"),
    path('logout',views.make_logout, name = "logout"), 
    path('signup',views.make_register, name = "signup"),
    path('change', views.make_change, name = 'change'),
] 