from django.shortcuts import render, redirect
from . import forms

def login(request):
    return render(request, 'login.html.jinja')

def logout(request):
    return render(request, 'logout.html.jinja')

def register(request):
    if request.method == 'GET':
        form = forms.RegistrationForm()
        address_formset = forms.UserAddressFormSet()
        return render(request, 'register.html.jinja', {'form': form, 'address_formset': address_formset})
    elif request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        return render(request, 'register.html.jinja', {'message': 'success'})
    else:
        return render(request, 'register.html.jinja', {'message': 'success'})
