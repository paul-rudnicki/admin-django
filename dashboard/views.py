from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('dashboard')
                else:
                    return HttpResponse('Konto zostało zablokowane')
            else:
                return HttpResponse('Nieprawidłowe dane logowania')
    else:
        form = LoginForm()

    return render(request, 'all/pages/login.html', {'form': form})


@login_required
def home(request):
    return render(request, 'dashboard/home.html')
