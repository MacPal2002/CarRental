from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# Create your models here.

class Equipment(models.Model):
    equipment = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.equipment
pass

class Car(models.Model):
    ENGINE_TYPES = [
        ("benzynowy", "Benzynowy"),
        ("diesel", "Diesel"),
        ("hybrydowy", "Hybrydowy"),
        ("elektryczny", "Elektryczny"),
        ("wodorowy", "Wodorowy")
    ]
    GEARBOX_TYPES = [
        ("automatyczna", "Automatyczna"),
        ("manualna", "Manualna"),
        ("pol_automatyczna", "Poł automatyczna"),
    ]
    CATEGORIES = [
        ("suv", "Suv"),
        ("miejski", "Miejski"),
        ("terenowy", "Terenowy"),
        ("van", "Van"),
        ("sportowy", "Sportowy"),
    ]
    category = models.CharField(max_length=50, choices=CATEGORIES, verbose_name='Kategoria')
    brand = models.CharField(max_length=50, verbose_name='Marka')
    model = models.CharField(max_length=50, verbose_name='Model')
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES, verbose_name='Typ silnika')
    seats_count = models.PositiveBigIntegerField(verbose_name='Ilość siedzeń')
    doors_count = models.PositiveSmallIntegerField(verbose_name='Ilość drzwi')
    fuel_usage = models.FloatField(verbose_name='Zużycie paliwa')
    engine_power = models.PositiveSmallIntegerField(verbose_name='Moc silnika')
    color = models.CharField(max_length=20, verbose_name='Kolor')
    equipment = models.ManyToManyField(Equipment, verbose_name='Wyposażenie')
    gearbox_types = models.CharField(max_length=20, choices=GEARBOX_TYPES, verbose_name='Typ skrzyni biegów')
    available = models.BooleanField(verbose_name='Dostępność')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Wartość')
    pass



class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    building_no = models.CharField(max_length=10)
    appartment_no = models.CharField(max_length=10, blank=True, default='', help_text='To pole jest opcjonalne.')
    pass

class User(User):
    IDENTITY_DOCUMENT_TYPES = [
        ("dowod", "Dowód osobisty"),
        ("passport", "Paszport"),
        ("prawo_jazdy", "Prawo jazdy"),
    ]
    phone = models.CharField(max_length=20)
    identity_document_no = models.CharField(max_length=20)
    identity_document_type = models.CharField(max_length=20, choices=IDENTITY_DOCUMENT_TYPES)
    pass


class Order(models.Model):
    PAYMENT_METHODS = [
        ("karta", "Karta"),
        ("gotowka", "Gotówka"),
        ("przelew", "Przelew"),
        ("blik", "Blik"),
    ]
    customer = models.ForeignKey(User, on_delete=models.RESTRICT)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    order_value = models.DecimalField(max_digits=10, decimal_places=2)
    declared_order_duration = models.DurationField()
    pickup_date = models.DateTimeField()
    return_date = models.DateTimeField()
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_status = models.BooleanField()
    pass

