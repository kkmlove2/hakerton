from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import loginForm, registerForm, changeForm
from django.contrib import messages

# Create your views here.

def start(request):
    return render(request, 'main.html')

def make_login(request):
    if request.method == "POST":
        complete_form = loginForm(request = request, data = request.POST)
        if complete_form.is_valid():
            user_id = complete_form.cleaned_data['username']
            user_pw = complete_form.cleaned_data['password']
            user = authenticate(request = request, username = user_id, password = user_pw)
            if user is not None: 
                login(request, user)
                return redirect('main')
        messages.error(request,'!ID, Password를 다시 확인해주세요!') 
        return redirect('login')


    else: 
        login_form = loginForm()
        return render(request, 'login.html', {'new_form' : login_form})

def make_logout(request):
    logout(request)
    return redirect('main')


def make_register(request):
    if request.method == 'POST':
        register_form = registerForm(request.POST)
        user = register_form.save()
        return redirect ('main')
    else:
        new_form = registerForm()
        return render (request, 'login.html', {'new_form':new_form})

def make_change(request):
    # unchanged_form = get_object_or_404(changeForm, pk = change)

    if request.method =='POST':
        change_form = changeForm(request.POST, instance = request.user)
        if change_form.is_valid():
            user = change_form.save()
            return redirect('main')
    else:
        newChange_form = changeForm(instance = request.user)
        return render(request,'login.html',{'new_form':newChange_form})

