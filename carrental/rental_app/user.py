from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.utils.translation import gettext_lazy as _

def login(request):
    next_url = request.GET.get('next', 'index')

    if request.method == 'GET':
        login_form = forms.LoginForm()
        return render(request, 'login.html.jinja', {'login_form': login_form, 'next': next_url})
    
    elif request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Autentykacja użytkownika
            if user is not None:
                auth_login(request, user)  # Logowanie użytkownika
                return redirect(next_url)
            else:
                # Obsługa nieudanego logowania
                login_form.add_error(None, _("Invalid username or password. Please try again."))

        # Jeśli formularz jest niepoprawny, ponowne wyświetlenie formularza z błędami
        return render(request, 'login.html.jinja', {'login_form': login_form, 'next': next_url})

def logout(request):
    auth_logout(request)
    return redirect('login') 

def register(request):
    if request.method == 'POST':
        user_form = forms.RegistrationForm(request.POST)
        address_form = forms.UserAddressFormSet(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            # Zapisz użytkownika
            user = user_form.save()
            # Zapisz adresy użytkownika
            addresses = address_form.save(commit=False)
            for address in addresses:
                address.user = user
                address.save()
            # Komunikat sukcesu
            return render(request, 'register.html.jinja', {'message': 'success'})
        else:
            # Wyświetl formularz z błędami
            return render(request, 'register.html.jinja', {'register_user_form': user_form, 'register_address_form': address_form})
    else:
        # Wyświetl pusty formularz
        user_form = forms.RegistrationForm()
        address_form = forms.UserAddressFormSet()
        return render(request, 'register.html.jinja', {'register_user_form': user_form, 'register_address_form': address_form})

