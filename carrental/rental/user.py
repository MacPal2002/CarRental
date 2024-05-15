from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User

def login(request):
    return render(request, 'login.html.jinja')

def logout(request):
    return render(request, 'logout.html.jinja')

def register(request):
    if request.method == 'POST':
        user_form = forms.RegistrationForm(request.POST)
        address_formset = forms.UserAddressFormSet(request.POST)
        if user_form.is_valid() and address_formset.is_valid():
            # Zapisz użytkownika
            user = user_form.save()
            # Zapisz adresy użytkownika
            addresses = address_formset.save(commit=False)
            for address in addresses:
                address.user = user
                address.save()
            # Komunikat sukcesu
            return render(request, 'register.html.jinja', {'message': 'success'})
        else:
            # Wyświetl formularz z błędami
            return render(request, 'register.html.jinja', {'user_form': user_form, 'address_formset': address_formset})
    else:
        # Wyświetl pusty formularz
        user_form = forms.RegistrationForm()
        address_formset = forms.UserAddressFormSet()
        return render(request, 'register.html.jinja', {'user_form': user_form, 'address_formset': address_formset})
