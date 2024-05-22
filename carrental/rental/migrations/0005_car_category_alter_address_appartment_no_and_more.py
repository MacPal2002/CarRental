# Generated by Django 5.0.3 on 2024-05-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_alter_address_appartment_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('suv', 'Suv'), ('miejski', 'Miejski'), ('terenowy', 'Terenowy'), ('van', 'Van'), ('sportowy', 'Sportowy')], default=None, max_length=50, verbose_name='Kategoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='appartment_no',
            field=models.CharField(blank=True, default='', help_text='To pole jest opcjonalne.', max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='available',
            field=models.BooleanField(verbose_name='Dostępność'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Marka'),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=20, verbose_name='Kolor'),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors_count',
            field=models.PositiveSmallIntegerField(verbose_name='Ilość drzwi'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_power',
            field=models.PositiveSmallIntegerField(verbose_name='Moc silnika'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_type',
            field=models.CharField(choices=[('benzynowy', 'Benzynowy'), ('diesel', 'Diesel'), ('hybrydowy', 'Hybrydowy'), ('elektryczny', 'Elektryczny'), ('wodorowy', 'Wodorowy')], max_length=20, verbose_name='Typ silnika'),
        ),
        migrations.AlterField(
            model_name='car',
            name='equipment',
            field=models.ManyToManyField(to='rental.equipment', verbose_name='Wyposażenie'),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_usage',
            field=models.FloatField(verbose_name='Zużycie paliwa'),
        ),
        migrations.AlterField(
            model_name='car',
            name='gearbox_types',
            field=models.CharField(choices=[('automatyczna', 'Automatyczna'), ('manualna', 'Manualna'), ('pol_automatyczna', 'Poł automatyczna')], max_length=20, verbose_name='Typ skrzyni biegów'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cena'),
        ),
        migrations.AlterField(
            model_name='car',
            name='seats_count',
            field=models.PositiveBigIntegerField(verbose_name='Ilość siedzeń'),
        ),
        migrations.AlterField(
            model_name='car',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Wartość'),
        ),
        migrations.AlterField(
            model_name='user',
            name='identity_document_type',
            field=models.CharField(choices=[('dowod', 'Dowód osobisty'), ('passport', 'Paszport'), ('prawo_jazdy', 'Prawo jazdy')], max_length=20),
        ),
    ]