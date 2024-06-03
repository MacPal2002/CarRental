from django.contrib import admin
from django.contrib.auth.models import User as AuthUser
from .models import Car, Equipment, UserData, Order, Address

# Klasa Inline dla adresu
class AddressInline(admin.StackedInline):
    model = Address
    can_delete = False # Czy można usuwać adresy powiązane z obiektem nadrzędnym


# Wyrejestrowanie domyślnego modelu użytkownika i ponowne zarejestrowanie niestandardowego
admin.site.unregister(AuthUser)
# Rejestruj modele w panelu admina
admin.site.register(Equipment)
admin.site.register(Car, list_display = (
    'id',
    'brand',
    'model',
    'color', 
    'price', 
    'engine_type', 
    'engine_power', 
    'gearbox_type', 
    'available', 
    'category',
))
admin.site.register(Order, list_display = (
    'id', 
    'customer', 
    'car', 
    'order_value', 
    'deposit', 
    'declared_order_duration', 
    'pickup_date', 
    'return_date', 
    'payment_method', 
    'payment_status' 
))
admin.site.register(UserData, inlines = (AddressInline,), list_display = (
    'username', 
    'first_name', 
    'last_name', 
    'email', 
    'phone', 
    'address', 
    'identity_document_type', 
    'identity_document_no' 
))
