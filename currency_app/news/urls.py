from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path("<int:news_id>/", views.news_details, name="news_details"),
    
]