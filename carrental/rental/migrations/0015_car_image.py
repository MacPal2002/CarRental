# Generated by Django 5.0.3 on 2024-06-04 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0014_alter_order_declared_order_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
