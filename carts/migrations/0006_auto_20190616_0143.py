# Generated by Django 2.1.7 on 2019-06-16 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_carrito_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='latitud',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='carrito',
            name='longitud',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='carrito',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
