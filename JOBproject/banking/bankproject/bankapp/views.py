from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def demo(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/account/')
        else:
            messages.error(request, 'Login Failed! Invalid username and password')
            return redirect('/login/')

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username', )
        password = request.POST.get('password', )
        cpassword = request.POST.get('cfpassword', )
        if password == cpassword:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            print("user created")
            return redirect('/login/')
        else:
            print('Invalid password')

    return render(request, 'register.html')


def account(request):
    if request.method == "POST":
        username = request.POST['username']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Application accepted')
            return redirect('/account/')
        else:
            messages.error(request, 'Application Submission Failed! Invalid username')
            return redirect('/')

    return render(request, 'account.html')
