# Generated by Django 5.0.3 on 2024-06-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0020_alter_order_declared_order_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='declared_order_duration',
            field=models.IntegerField(null=True, verbose_name='Declared rental duration'),
        ),
    ]
