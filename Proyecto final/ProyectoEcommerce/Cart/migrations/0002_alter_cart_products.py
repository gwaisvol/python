# Generated by Django 4.1.7 on 2023-03-28 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.CharField(choices=[('Peluche', 'Peluche'), ('gps', 'gps'), ('Radio', 'Radio'), ('Rompecabezas', 'Rompecabezas'), ('Alarma', 'Alarma'), ('Libro', 'Libro')], max_length=90),
        ),
    ]
