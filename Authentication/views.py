from django.shortcuts import render, redirect
from Authentication import models


# Create your views here.


def login(request):
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = ""
        if username and password:
            try:
                user = models.UserInfo.objects.get(username=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/')
                else:
                    message = "Wrong Password"
            except:
                message = "User " + str(username) + " doesn't exist."
        else:
            message = "Please fill up the forms"
        return render(request, 'Authentication/Login.html', {"message": message})

    return render(request, 'Authentication/Login.html')


def signup(request):
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == "POST":
        print(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = ""
        if username and password and email:
            if models.UserInfo.objects.filter(email=email):
                message = "Email has already been registered!"
                return render(request, 'Authentication/Signup.html', {"message": message})
            if models.UserInfo.objects.filter(username=username):
                message = "Username has already been registered!"
                return render(request, 'Authentication/Signup.html', {"message": message})

            new_user = models.UserInfo.objects.create()
            new_user.email = email
            new_user.username = username
            new_user.password = password
            new_user.save()

            return redirect('/login')
        else:
            message = "Please fill up the forms"
            return render(request, 'Authentication/Signup.html', {"message": message})

    return render(request, 'Authentication/Signup.html')


def logout(request):
    request.session['is_login'] = False
    return redirect('/')
