# Generated by Django 2.1.7 on 2019-06-17 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_auto_20190616_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, height_field=100, upload_to='producto/%Y/%m/%d', width_field=150),
        ),
    ]
