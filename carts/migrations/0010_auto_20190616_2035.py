# Generated by Django 2.1.7 on 2019-06-17 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_auto_20190616_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='height',
            field=models.PositiveIntegerField(default=100, null=True),
        ),
        migrations.AddField(
            model_name='productos',
            name='width',
            field=models.PositiveIntegerField(default=150, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, height_field='height', upload_to='producto/%Y/%m/%d', width_field='width'),
        ),
    ]