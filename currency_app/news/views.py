from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import News


def news_details(request, news_id):
    post = News.objects.get(id=news_id)
    template = loader.get_template("news/news.html")
    return HttpResponse(template.render({"post": post}, request))
