from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from . models import Profile
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('conpassword')

        if password != password2:
            messages.error(request, "password does not match")
            return redirect('user:register')
        
        if User.objects.filter(username = username).exists():
            messages.error(request, "username is already taken")
            return redirect('user:register')
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "email already exists")
            return redirect('user:register')
        
        if len(username) < 8:
            messages.error(request, "username must be at least 8 characters long")
            return redirect('user:register')
        
        if len(password) < 8:
            messages.error(request, "password must be at least 8 characters long")
            return redirect('user:register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        img = Profile.objects.create(user=user)
        user.save()
        img.save()
        messages.success(request, "succesfully registered")
        return redirect('user:login')
    return render(request, "user/register.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have been successfully logged in.")
            return redirect('index')
        else:
            messages.error(request, "incorrect username or password.")
            return redirect('user:login')
    return render(request, "user/login.html")


def user_logout(request):
    logout(request)
    return redirect('user')

def user_profile(request):
    edit = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user__username=request.user.username)
    if request.method == 'POST':
        profile.image = request.FILES.get('image') or profile.image
        edit.username = request.POST.get('fname')
        edit.email = request.POST.get('email')
        profile.save()
        edit.save()
        return redirect('index')
    context = {
        'edited':edit,
        'profiled':profile
    }

    return render(request, "user/profile.html", context)