from django.contrib import admin

# Register your models here.
from .models import Car,Equipment

admin.site.register(Car)
admin.site.register(Equipment)

