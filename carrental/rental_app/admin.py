from django.contrib import admin
from .models import Car, Equipment, UserData, Order, Address
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class AddressInline(admin.StackedInline):
    model = Address
    can_delete = False
    verbose_name_plural = _("Address")


class CustomUserAdmin(UserAdmin):
    inlines = (AddressInline,)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        "identity_document_type",
        "identity_document_no",
        "is_staff",
    )

    fieldsets = list(UserAdmin.fieldsets) + [
        (
            _("Additional Info"),
            {"fields": ("phone", "identity_document_no", "identity_document_type")},
        ),
    ]
    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        (
            _("Additional Info"),
            {"fields": ("phone", "identity_document_no", "identity_document_type")},
        ),
    ]


# Rejestracja modeli
admin.site.register(UserData, CustomUserAdmin)
admin.site.register(Equipment)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "brand",
        "model",
        "color",
        "price",
        "engine_type",
        "engine_power",
        "gearbox_type",
        "available",
        "category",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "car",
        "order_value",
        "deposit",
        "declared_order_duration",
        "pickup_date",
        "return_date",
        "payment_method",
        "payment_status",
    )
