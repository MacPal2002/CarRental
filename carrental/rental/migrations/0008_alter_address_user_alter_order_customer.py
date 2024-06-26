# Generated by Django 5.0.3 on 2024-05-22 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0007_rentaluser_alter_order_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rental.rentaluser', verbose_name='użytkownik'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rental.rentaluser', verbose_name='Klient'),
        ),
    ]
