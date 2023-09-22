from allauth.account.views import LoginView
from django.shortcuts import render, HttpResponse



def Home(request):
    return render(request, 'index.html')