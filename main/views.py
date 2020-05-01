from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from .models import Account
from certificates.forms import CertificateForm
from certificates.models import Certificate


def home_screen_view(request):
    accounts = Account.objects.all()
    filed_certificates = Certificate.objects.all()

    context = {
        'accounts': accounts,
        'filed_certificates': filed_certificates,
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
    certificate_form = CertificateForm()

    if request.POST:
        account_form = AccountUpdateForm(request.POST, instance=request.user)
        if account_form.is_valid():
            account_form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            account_form.save()
            success_massage = "Updated"
    else:
        account_form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context = {
        'account_form': account_form,
        'certificate_form': certificate_form,
        'success_message': success_massage,
        'certificates': Certificate.objects.filter(hospital=request.user.hospital)
    }
    return render(request, 'account.html', context)
