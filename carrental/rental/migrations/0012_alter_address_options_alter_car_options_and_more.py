# Generated by Django 5.0.3 on 2024-05-24 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0018_alter_userdata_options_and_more'),
        ('rental', '0011_alter_car_gearbox_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name': 'Equipment', 'verbose_name_plural': 'Equipments'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterField(
            model_name='address',
            name='appartment_no',
            field=models.CharField(blank=True, default='', help_text='This field is optional.', max_length=10, verbose_name='Apartment number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='building_no',
            field=models.CharField(max_length=10, verbose_name='Building number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=30, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=30, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='address',
            name='post_code',
            field=models.CharField(max_length=10, verbose_name='Post code'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=50, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.userdata', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='car',
            name='available',
            field=models.BooleanField(verbose_name='Availability'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('suv', 'SUV'), ('city', 'City'), ('off-road', 'Off-road'), ('van', 'Van'), ('sports', 'Sports')], max_length=50, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=20, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors_count',
            field=models.PositiveSmallIntegerField(verbose_name='Number of doors'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_power',
            field=models.PositiveSmallIntegerField(verbose_name='Engine power'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_type',
            field=models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('hybrid', 'Hybrid'), ('electric', 'Electric'), ('hydrogen', 'Hydrogen')], max_length=20, verbose_name='Engine type'),
        ),
        migrations.AlterField(
            model_name='car',
            name='equipment',
            field=models.ManyToManyField(to='rental.equipment', verbose_name='Equipment'),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_usage',
            field=models.FloatField(verbose_name='Fuel consumption'),
        ),
        migrations.AlterField(
            model_name='car',
            name='gearbox_type',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual'), ('semi-automatic', 'Semi-automatic')], max_length=20, verbose_name='Gearbox type'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='car',
            name='seats_count',
            field=models.PositiveBigIntegerField(verbose_name='Number of seats'),
        ),
        migrations.AlterField(
            model_name='car',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment',
            field=models.CharField(max_length=50, verbose_name='Equipment'),
        ),
        migrations.AlterField(
            model_name='order',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rental.car', verbose_name='Car'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='auth.userdata', verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='declared_order_duration',
            field=models.DurationField(verbose_name='Declared rental duration'),
        ),
        migrations.AlterField(
            model_name='order',
            name='deposit',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Deposit'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Order value'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('card', 'Card'), ('cash', 'Cash'), ('transfer', 'Transfer'), ('blik', 'Blik')], max_length=20, verbose_name='Payment method'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(verbose_name='Payment status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pickup_date',
            field=models.DateTimeField(verbose_name='Pickup date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='return_date',
            field=models.DateTimeField(verbose_name='Return date'),
        ),
    ]
