import pandas as pd
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Car, Order, UserData
from . import forms
import random


# Create your views here.

def index(request):
    recommended_cars = Car.objects.order_by('-id')[:4]

    # Pobierz najczęściej wybierane samochody
    popular_cars = Order.objects.values('car').annotate(car_count=Count('car')).order_by('-car_count')
    
    # Przekształć popular_cars do listy car_ids
    popular_car_ids = [item['car'] for item in popular_cars]
    
    # Pobierz obiekty Car dla tych IDs
    popular_car_objects = list(Car.objects.filter(id__in=popular_car_ids)[:4])

    # Jeśli liczba popularnych samochodów jest mniejsza niż 4, wylosuj dodatkowe
    if len(popular_car_objects) < 4:
        # Pobierz IDs już wybranych samochodów
        chosen_car_ids = [car.id for car in popular_car_objects]
        # Pobierz dostępne samochody, które nie są jeszcze wybrane
        additional_cars = list(Car.objects.exclude(id__in=chosen_car_ids))
        # Wylosuj brakującą liczbę samochodów
        random.shuffle(additional_cars)
        additional_car_objects = additional_cars[:4 - len(popular_car_objects)]
        # Dodaj je do listy popular_car_objects
        popular_car_objects.extend(additional_car_objects)

    return render(request, 'index.html.jinja', {'recommended_cars': recommended_cars, 'popular_cars': popular_car_objects})


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


@login_required
def rent(request, car_id):
    # Sprawdź, czy istnieje samochód o podanym ID
    car = get_object_or_404(Car, id=car_id)

    # Pobierz bieżącego użytkownika
    current_user = UserData.objects.get(id=request.user.id)

    initial_deposit = 0.1 * float(car.value)
    
    if request.method == 'POST':
        order_form = forms.OrderForm(request.POST)
        if order_form.is_valid():
            # Zapisz zamówienie
            order = order_form.save(commit=False)
            order.car = car
            order.deposit = initial_deposit
            order.customer = current_user  # Ustaw bieżącego użytkownika jako klienta
            order.save()
            return redirect('confirm', order=order)
        else:
            # Wyświetl formularz z błędami
            return render(request, 'rent.html.jinja', {'order_form': order_form, 'car_id': car_id, 'car_price': car.price})
    else:
        # Utwórz formularz dla nowego zamówienia
        order_form = forms.OrderForm(initial={'car': car.id, 'deposit': initial_deposit, 'customer': current_user.id})
        return render(request, 'rent.html.jinja', {'order_form': order_form, 'car_id': car_id, 'car_price': str(car.price)})
    


@login_required
def confirm(request, order):
    return render(request, 'confirm.html.jinja', {'order': order})