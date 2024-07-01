from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from counter.get_currencyes import get_currencies_values
from counter.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import News




def index(request):
    value = get_currencies_values()
    currency_names = value.keys()
    if request.method == "POST":
         from_ = request.POST['from_']
         to = request.POST['to']
         sum = request.POST['sum']
        
         if sum.isdigit() and (from_!='Выбрать...' and to!='Выбрать...') and (from_!=to):
          value = round((float(sum)*float(value[from_][1].replace(',','.'))/float(value[from_][0]))*float(value[to][0])/float(value[to][1].replace(',','.')),4)

         elif not sum or sum.isdigit()==False:
            value = 'Пожалуйста, введите корректное значение'
            to = ''

         elif from_==to or from_=='Выбрать...' or to=='Выбрать...':
           value='Выберите разные валюты для конвертации'
           to = ''
           
         template = loader.get_template("counter/index.html")
         context = {"get_curr": currency_names,
               "value": value,
               "c_name": to}

         return HttpResponse(template.render(context, request))
 
    
    template = loader.get_template("counter/index.html")
    context = {"get_curr": currency_names,
               "value": ""}

    return HttpResponse(template.render(context, request))

def register(request):
   template = loader.get_template("counter/register.html")

   if request.method == 'POST':
        user_form = RegisterForm(request.POST)

        if user_form.is_valid():
            username = user_form.cleaned_data.get("username")
            password = user_form.cleaned_data.get("password")
            
            user = User.objects.create_user(username, password)

            user.set_password(password)
            user.save()

            if user is not None:
              login(request, user)

              return redirect('/')
          

   return HttpResponse(template.render({}, request))

def login_user(request):
    template = loader.get_template("counter/login.html")

    if request.method == 'POST':
             user_form = LoginForm(request.POST)
             if user_form.is_valid():
               
               username = user_form.cleaned_data.get("username_")
               password = user_form.cleaned_data.get("password_")
              
               user = authenticate(request, username=username,password=password)

               if user is not None:
                 login(request, user)

                 return redirect('/')
               
               else:
                    messages.error(request, 'Неверный логин или пароль')
            
    return HttpResponse(template.render({}, request))

def logout_view(request):
    logout(request)

    return redirect('/')


def base(request):
     posts = News.objects.all()
     template = loader.get_template("counter/main.html")
     return HttpResponse(template.render({"posts": posts}, request))
