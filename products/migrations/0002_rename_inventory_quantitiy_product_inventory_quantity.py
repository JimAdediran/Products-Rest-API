# Generated by Django 4.0.5 on 2022-07-04 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='inventory_quantitiy',
            new_name='inventory_quantity',
        ),
    ]
