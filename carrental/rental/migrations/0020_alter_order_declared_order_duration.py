# Generated by Django 5.0.3 on 2024-06-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0019_alter_car_image_alter_order_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='declared_order_duration',
            field=models.IntegerField(blank=True, verbose_name='Declared rental duration'),
        ),
    ]
