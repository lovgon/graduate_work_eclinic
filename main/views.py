from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from .models import Account


def home_screen_view(request):
    accounts = Account.objects.all()

    context = {
        'accounts': accounts,
    }

    return render(request, 'index.html', context)


def registration_view(request):
    user = request.user

    if user.is_authenticated:
        return redirect("account")

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context = {'registration_form': form}
    else:  # GET request
        form = RegistrationForm()
        context = {'registration_form': form}
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    user = request.user

    if user.is_authenticated:
        return redirect("account")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("account")
    else:
        form = AccountAuthenticationForm()

    context = {'login_form': form}

    return render(request, 'login.html', context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    success_massage = 0

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            success_massage = "Updated"
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context = {
        'account_form': form,
        'success_message': success_massage,
    }
    return render(request, 'account.html', context)
