# Generated by Django 2.1.7 on 2019-06-14 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20190613_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='fecha_nacimiento',
        ),
    ]
