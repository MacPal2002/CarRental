from django.db import models

# Create your models here.

class Equipment(models.Model):
    equipment = models.CharField(max_length=50)
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
        ("polautomatyczna", "Polautomatyczna"),
    ]
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES)
    seats_count = models.PositiveBigIntegerField()
    doors_count = models.PositiveSmallIntegerField()
    fuel_usage = models.FloatField()
    engine_power = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=20)
    equipment = models.ManyToManyField(Equipment)
    gearbox_types = models.CharField(max_length=20, choices=GEARBOX_TYPES)
    available = models.BooleanField()
    pass

class User(models.Model):
    pass

class Order(models.Model):
    PAYMENT_METHODS = [
        ("karta", "Karta"),
        ("gotowka", "Gotowka"),
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


