from django.shortcuts import render, redirect 
from django.contrib.auth import  login, logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from account.forms import SignUpForm 
from account.sendgmail import send_forget_password_mail
from account.models import *

# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.warning(request, "user does not exist!")
                    return redirect('/login')
            else:
                messages.add_message(request, messages.ERROR, "Make sure you entered valid username and password and try again.")
        
        form = AuthenticationForm()
        context = {'form': form ,}
        return render(request, 'account/login.html', context)
    else:
        return redirect('/')
    
def logout_view(request):
    if request.user.is_authenticated:  
        logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                if User.objects.filter(username=username).first():
                    messages.error(request, "Username is taken")
                    return redirect('/signup')
                if User.objects.filter(email=email).first():
                    messages.error(request, "Email is taken")
                    return redirect('/signup')
                else:
                    form.save()
                    messages.add_message(request, messages.SUCCESS, "Congrats! Your account created successfully.")
                    return redirect('/login')
            else:
                messages.add_message(request, messages.ERROR, "Make sure you entered valid username, password, and confirm password then try again.")
    else: 
        return redirect('/')

    form = SignUpForm()
    context = {'form': form ,}
    return render(request, 'account/signup.html', context)

import uuid
def forget_password_view(request):
    if not request.user.is_authenticated:
        try:
            if request.method == 'POST':
                username1 = request.POST.get('username')
                user = User.objects.filter(username=username1).first()
                user1 = User.objects.filter(email=username1).first()
                if user is None and user1 is None:
                    messages.warning(request, "User doesn't exist!")
                    return redirect('/forget-password')
                elif user != None:
                    user_obj = User.objects.get(username= username1)
                    print(user_obj)
                    token = str(uuid.uuid4())
                    profile_obj = Profile(user=user_obj , forget_password_token = token)
                    profile_obj.save()
                    send_forget_password_mail(user_obj.email, token)
                    messages.add_message(request, messages.SUCCESS, "An email is sent.")

                elif user1 != None:
                    user_obj = User.objects.get(email= username1)
                    token = str(uuid.uuid4())
                    profile_obj = Profile(user=user_obj , forget_password_token = token)
                    profile_obj.save()
                    send_forget_password_mail(user_obj.email, token)
                    messages.add_message(request, messages.SUCCESS, "An email is sent.")
        except Exception as e:
            print(e)   
    return render(request, 'account/forget-password.html')


def reset_password_view(request, token):
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        if request.method == 'POST':
            new_password = request.POST.get('password1')
            confirm_password = request.POST.get('password2')
            user_id = request.POST.get('user_id')
            if user_id is None:
                messages.warning(request, "No user id found!")
                return redirect(f'/reset-password/{token}/')
            if new_password != confirm_password:
                messages.warning(request, "please confirm your password correctly.")
                return redirect(f'/reset-password/{token}/')
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            print(type(user_obj), user_obj, new_password)
            user_obj.save()
            return redirect('account:login')
        
    except Exception as e:
        print(e)
    context = {'user_id': profile_obj.user_id, 'token': token}
    return render(request, 'account/reset-password.html', context)
