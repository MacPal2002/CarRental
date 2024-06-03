import pandas as pd
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Car, Order
from . import forms


# Create your views here.

def index(request):
    return render(request, 'index.html.jinja')


def cars(request):
    cars = Car.objects.all()
    cars_table = pd.DataFrame.from_records(cars.values())

    # Słownik mapujący kategorie na ich przyjazne użytkownikowi nazwy
    category_dict = dict(Car.CATEGORIES)

    # Tworzenie struktury danych dla szablonu
    cars_by_category = {}
    for car in cars:
        category_name = category_dict[car.category]
        if category_name not in cars_by_category:
            cars_by_category[category_name] = []
        cars_by_category[category_name].append(car)

    return render(request, 'cars.html.jinja', {'cars_by_category': cars_by_category, 'cars_table': cars_table.to_html(classes='table table-striped table-bordereds', index=False, table_id='cars_table')}, )

def car(request, car_id):
    return render(request, 'car.html.jinja')

def rent(request, car_id):

    # Sprawdź, czy istnieje samochód o podanym ID
    car = get_object_or_404(Car, id=car_id)

    initial_deposit = 0.1 * float(car.value)
    
    if request.method == 'POST':
        order_form = forms.OrderForm(request.POST)
        if order_form.is_valid():
            # Zapisz zamówienie
            order = order_form.save(commit=False)
            order.car = car
            order.deposit = initial_deposit
            order.save()
            return redirect('confirm', order=order)
        else:
            # Wyświetl formularz z błędami
            return render(request, 'rent.html.jinja', {'order_form': order_form, 'car_id': car_id})
    else:
        # Utwórz formularz dla nowego zamówienia
        order_form = forms.OrderForm(initial={'car': car.id, 'deposit': initial_deposit})
        return render(request, 'rent.html.jinja', {'order_form': order_form, 'car_id': car_id})
    



def confirm(request, order):
    return render(request, 'confirm.html.jinja', {'order': order})