from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Equipment(models.Model):
    equipment = models.CharField(max_length=50, verbose_name=_('Wyposażenie'))

    def __str__(self) -> str:
        return self.equipment

    class Meta:
        verbose_name = _("Wyposażenie")
        verbose_name_plural = _("Wyposażenia")


class Car(models.Model):
    ENGINE_TYPES = [
        ("benzynowy", _("Benzynowy")),
        ("diesel", _("Diesel")),
        ("hybrydowy", _("Hybrydowy")),
        ("elektryczny", _("Elektryczny")),
        ("wodorowy", _("Wodorowy"))
    ]
    GEARBOX_TYPES = [
        ("automatyczna", _("Automatyczna")),
        ("manualna", _("Manualna")),
        ("pol_automatyczna", _("Poł automatyczna")),
    ]
    CATEGORIES = [
        ("suv", _("Suv")),
        ("miejski", _("Miejski")),
        ("terenowy", _("Terenowy")),
        ("van", _("Van")),
        ("sportowy", _("Sportowy")),
    ]
    category = models.CharField(max_length=50, choices=CATEGORIES, verbose_name=_('Kategoria'))
    brand = models.CharField(max_length=50, verbose_name=_('Marka'))
    model = models.CharField(max_length=50, verbose_name=_('Model'))
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES, verbose_name=_('Typ silnika'))
    seats_count = models.PositiveBigIntegerField(verbose_name=_('Ilość siedzeń'))
    doors_count = models.PositiveSmallIntegerField(verbose_name=_('Ilość drzwi'))
    fuel_usage = models.FloatField(verbose_name=_('Zużycie paliwa'))
    engine_power = models.PositiveSmallIntegerField(verbose_name=_('Moc silnika'))
    color = models.CharField(max_length=20, verbose_name=_('Kolor'))
    equipment = models.ManyToManyField(Equipment, verbose_name=_('Wyposażenie'))
    gearbox_types = models.CharField(max_length=20, choices=GEARBOX_TYPES, verbose_name=_('Typ skrzyni biegów'))
    available = models.BooleanField(verbose_name=_('Dostępność'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Cena'))
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Wartość'))

    def __str__(self) -> str:
        return f"{self.brand} {self.model} (ID: {self.id})"

    class Meta:
        verbose_name = _("Samochód")
        verbose_name_plural = _("Samochody")


class UserData(User):
    IDENTITY_DOCUMENT_TYPES = [
        ("dowod", _("Dowód osobisty")),
        ("passport", _("Paszport")),
        ("prawo_jazdy", _("Prawo jazdy")),
    ]
    phone = models.CharField(max_length=20, verbose_name=_('Numer telefonu'))
    identity_document_no = models.CharField(max_length=20, verbose_name=_('Numer dokumentu tożsamości'))
    identity_document_type = models.CharField(max_length=20, choices=IDENTITY_DOCUMENT_TYPES, verbose_name=_('Typ dokumentu tożsamości'))

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.username})"

    class Meta:
        verbose_name = _("Dane użytkownika")
        verbose_name_plural = _("Dane użytkowników (Rental)")
        app_label = 'auth'


class Address(models.Model):
    user = models.OneToOneField(UserData, on_delete=models.CASCADE, verbose_name=_('użytkownik'))
    country = models.CharField(max_length=30, verbose_name=_('Kraj'))
    city = models.CharField(max_length=30, verbose_name=_('Miasto'))
    post_code = models.CharField(max_length=10, verbose_name=_('Kod pocztowy'))
    street = models.CharField(max_length=50, verbose_name=_('Ulica'))
    building_no = models.CharField(max_length=10, verbose_name=_('Numer budynku'))
    appartment_no = models.CharField(max_length=10, blank=True, default='', help_text=_('To pole jest opcjonalne.'), verbose_name=_('Numer mieszkania'))

    def __str__(self) -> str:
        if self.appartment_no:
            return f"{self.street} {self.building_no} / {self.appartment_no}, {self.post_code} {self.city}, {self.country}"
        else:
            return f"{self.street} {self.building_no}, {self.post_code} {self.city}, {self.country}"

    class Meta:
        verbose_name = _("Adres")
        verbose_name_plural = _("Adresy")

class Order(models.Model):
    PAYMENT_METHODS = [
        ("karta", _("Karta")),
        ("gotowka", _("Gotówka")),
        ("przelew", _("Przelew")),
        ("blik", _("Blik")),
    ]
    customer = models.ForeignKey(UserData, on_delete=models.RESTRICT, verbose_name=_('Klient'))
    car = models.ForeignKey(Car, on_delete=models.RESTRICT, verbose_name=_('Samochód'))
    order_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Wartość zamówienia'))
    declared_order_duration = models.DurationField(verbose_name=_('Deklarowany czas wypożyczenia'))
    pickup_date = models.DateTimeField(verbose_name=_('Data odebrania'))
    return_date = models.DateTimeField(verbose_name=_('Data zwrotu'))
    deposit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Depozyt'))
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, verbose_name=_('Metoda płatności'))
    payment_status = models.BooleanField(verbose_name=_('Status płatności'))

    def __str__(self) -> str:
        return f"Zam. ID: {self.id} ({'Opłacone' if self.payment_status else 'Nieopłacone'})"

    class Meta:
        verbose_name = _("Zamówienie")
        verbose_name_plural = _("Zamówienia")
