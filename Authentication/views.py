from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, 'Authentication/Login.html')


def signup(request):
    return render(request, 'Authentication/Signup.html')
