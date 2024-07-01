from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_view, name="logout"),
]