from allauth.account.views import LoginView
from django.shortcuts import render, HttpResponse

class MyLoginView(LoginView):
    def __init__(self, *args, **kwargs):
        super(MyLoginView, self).__init__(*args, **kwargs)
        print(self)

def Home(request):
    return HttpResponse("Connected")