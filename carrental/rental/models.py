from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image

class Equipment(models.Model):
    equipment = models.CharField(max_length=50, verbose_name=_('Equipment'))

    def __str__(self) -> str:
        return self.equipment

    class Meta:
        verbose_name = _("Equipment")
        verbose_name_plural = _("Equipments")

class Car(models.Model):
    ENGINE_TYPES = [
        ("petrol", _("Petrol")),
        ("diesel", _("Diesel")),
        ("hybrid", _("Hybrid")),
        ("electric", _("Electric")),
        ("hydrogen", _("Hydrogen"))
    ]
    GEARBOX_TYPES = [
        ("automatic", _("Automatic")),
        ("manual", _("Manual")),
        ("semi-automatic", _("Semi-automatic")),
    ]
    CATEGORIES = [
        ("suv", _("SUV")),
        ("city-friendly", _("City-friendly")),
        ("off-road", _("Off-road")),
        ("van", _("Van")),
        ("sports", _("Sports")),
    ]
    category = models.CharField(max_length=50, choices=CATEGORIES, verbose_name=_('Category'))
    image = models.ImageField(upload_to='images', default='images/default_image.jpg', verbose_name=_('Image'))
    brand = models.CharField(max_length=50, verbose_name=_('Brand'))
    model = models.CharField(max_length=50, verbose_name=_('Model'))
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES, verbose_name=_('Engine type'))
    seats_count = models.PositiveBigIntegerField(verbose_name=_('Number of seats'))
    doors_count = models.PositiveSmallIntegerField(verbose_name=_('Number of doors'))
    fuel_usage = models.FloatField(verbose_name=_('Fuel consumption'))
    engine_power = models.PositiveSmallIntegerField(verbose_name=_('Engine power'))
    color = models.CharField(max_length=20, verbose_name=_('Color'))
    equipment = models.ManyToManyField(Equipment, verbose_name=_('Equipment'))
    gearbox_type = models.CharField(max_length=20, choices=GEARBOX_TYPES, verbose_name=_('Gearbox type'))
    available = models.BooleanField(verbose_name=_('Availability'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Value'))

    def __str__(self) -> str:
        return f"{self.brand} {self.model} (ID: {self.id})"

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_car = Car.objects.get(pk=self.pk)
                if old_car.image != self.image:
                    old_car.image.delete(save=False)
            except Car.DoesNotExist:
                pass

        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        # Docelowa szerokość obrazu
        desired_width = 800

        # Docelowa proporcja obrazu
        desired_ratio = 330.75 / 186.05

        # Obliczanie docelowej wysokości przy zachowaniu proporcji
        desired_height = int(desired_width / desired_ratio)

        # Skalowanie obrazu do docelowych wymiarów
        img = img.resize((desired_width, desired_height))

        # Zapisanie przeskalowanego obrazu na tej samej ścieżce
        img.save(self.image.path)


class UserData(User):
    IDENTITY_DOCUMENT_TYPES = [
        ("identity_card", _("Identity card")),
        ("passport", _("Passport")),
        ("driver_license", _("Driver's license")),
    ]
    phone = models.CharField(max_length=20, verbose_name=_('Phone number'))
    identity_document_no = models.CharField(max_length=20, verbose_name=_('Identity document number'))
    identity_document_type = models.CharField(max_length=20, choices=IDENTITY_DOCUMENT_TYPES, verbose_name=_('Identity document type'))

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.username})"

    class Meta:
        verbose_name = _("User data")
        verbose_name_plural = _("User data (Rental)")
        app_label = 'auth'

class Address(models.Model):
    user = models.OneToOneField(UserData, on_delete=models.CASCADE, verbose_name=_('User'))
    country = models.CharField(max_length=30, verbose_name=_('Country'))
    city = models.CharField(max_length=30, verbose_name=_('City'))
    post_code = models.CharField(max_length=10, verbose_name=_('Post code'))
    street = models.CharField(max_length=50, verbose_name=_('Street'))
    building_no = models.CharField(max_length=10, verbose_name=_('Building number'))
    appartment_no = models.CharField(max_length=10, blank=True, default='', help_text=_('This field is optional.'), verbose_name=_('Apartment number'))

    def __str__(self) -> str:
        if self.appartment_no:
            return f"{self.street} {self.building_no} / {self.appartment_no}, {self.post_code} {self.city}, {self.country}"
        else:
            return f"{self.street} {self.building_no}, {self.post_code} {self.city}, {self.country}"

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

class Order(models.Model):
    PAYMENT_METHODS = [
        ("card", _("Card")),
        ("cash", _("Cash")),
        ("transfer", _("Transfer")),
        ("blik", _("Blik")),
    ]
    customer = models.ForeignKey(UserData, on_delete=models.RESTRICT, verbose_name=_('Customer'))
    car = models.ForeignKey(Car, on_delete=models.RESTRICT, verbose_name=_('Car'))
    order_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Order value'))
    declared_order_duration = models.IntegerField(null=True, verbose_name=_('Declared rental duration'))
    pickup_date = models.DateTimeField(verbose_name=_('Pickup date'))
    return_date = models.DateTimeField(verbose_name=_('Return date'))
    deposit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Deposit'))
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, verbose_name=_('Payment method'))
    payment_status = models.BooleanField(default=False, verbose_name=_('Payment status'))

    def __str__(self) -> str:
        return f"order-id:{self.id}"
    def clean(self):
        """
        Walidacja dat odbioru i zwrotu zamówienia.
        """
        if self.pickup_date >= self.return_date:
            raise ValidationError(_('Return date must be later than pickup date.'))

        from django.utils import timezone
        if self.pickup_date < timezone.now() or self.return_date < timezone.now():
            raise ValidationError(_('Dates must be greater than today\'s date.'))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
