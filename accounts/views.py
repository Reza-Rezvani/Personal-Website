from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django .contrib.auth.forms import AuthenticationForm,UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django .contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
# Create your views here.

    


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password) 
                if user is not None:
                    login(request,user)
                    return redirect('/')

        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = UserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')


#def update_user(request):
 #   return render(request, 'accounts/update_user.html', {})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UserChangeForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, 'User has been updated')
            return redirect('/')
        form = UserChangeForm()
        context = {'form':form}
        return render(request,'accounts/update_user.html',context)
    else:
        return redirect('/')