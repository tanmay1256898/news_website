from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from .forms import *
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import categore,zeenews,cricketlivescore,Contact
import feedparser
import mysql.connector
import requests
from newsapi import NewsApiClient
# Create your views here.

def loginPage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' wecome {username} !!')
			return redirect('accounts:home')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = CreateUserForm()
	return render(request, 'accounts/loginpage.html', {'form':form, 'title':'log in'})


def registerPage(request):
	if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, f'Your account has been created. You can log in now!')    
				return redirect('accounts:home')
	else:
		form = CreateUserForm()
	return render(request, 'accounts/registerpage.html', {'form' : form})

@login_required
def logoutUser(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("accounts:home")


def profile( request):
	return render(request, 'accounts/profile.html')
def TOI(request):
    categores = categore.objects.all()
    
    return render(request, 'accounts/TOI.html',{'categore':categores})

def Zeenews(request):
    categores = zeenews.objects.all()
    
    return render(request, 'accounts/zeenews.html',{'zeenews':categores})

def Cricket(request):
    categores = cricketlivescore.objects.all()
    
    return render(request, 'accounts/cricketlivescore.html',{'cricketlivescore':categores})
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        contact = Contact(name=name, email=email, phone=phone, description=description, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'accounts/contact.html')

def home( request):
	return render(request, 'accounts/home.html')

def rss(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = (f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey=759f3e7c59114bc8a9c14539a40fa625")
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = (f"https://newsapi.org/v2/top-headlines?country=in&apiKey=759f3e7c59114bc8a9c14539a40fa625")
        response = requests.get(url)
        data = response.json()
        articles = data['articles']



    context = {
        'articles' : articles
    }
    return render(request, "accounts/rss.html", context)

def live_score(request):
    # Make an HTTP request to the API
    response = requests.get('https://api.cricapi.com/v1/countries?apikey=6d6b98e1-9adf-42a0-b7b6-8f83f596bf16&offset=.$offset')
    data = response.json()
    
    # Pass the data to the template
    context = {'item': data}
    return render(request, 'accounts/live_score.html', context)

def test(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = (f"https://newsapi.org/v2/top-headlines?country=in&apiKey=759f3e7c59114bc8a9c14539a40fa625")
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = (f"https://newsapi.org/v2/top-headlines?country=in&apiKey=759f3e7c59114bc8a9c14539a40fa625")
        response = requests.get(url)
        data = response.json()
        articles = data['articles']



    context = {
        'articles' : articles
    }

    return render(request, "accounts/test.html", context)
    
def business(request):
    country = request.GET.get('country')
    category = request.GET.get('category')


    url = (f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=759f3e7c59114bc8a9c14539a40fa625")
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    



    context = {
        'articles' : articles
    }

    return render(request, "accounts/business.html", context)


