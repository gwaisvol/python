# Generated by Django 4.1.7 on 2023-03-28 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('products', models.CharField(choices=[], max_length=90)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
