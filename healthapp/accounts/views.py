from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'],
                            password = form.cleaned_data['password'])
            if user:
                print("A user is found---->", user)
                login(request, user)
                return redirect('/accounts/profile/')
            else:
                print("AUTH CREDENTIALS DO NOT MATCH!")
            print(form.cleaned_data)
            pass
    elif request.method == 'GET':
        form = LoginForm()
      
    return render(request, 'accounts/login.html/', {'form': form})

from django.contrib.auth.models import User
@login_required()
def profile_view(request):
    return render(request, 'accounts/profile.html')


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(" 'SIGNUP FORM IS VALID!' ")
            print(form.cleaned_data)
            user = User(
                username=form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                password = form.cleaned_data['password']
            )
            user.save()
            # making user password hash
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/accounts/login/')
        else:
            pass
       
    elif request.method == 'GET':
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})



