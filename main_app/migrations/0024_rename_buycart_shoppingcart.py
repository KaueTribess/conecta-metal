# Generated by Django 5.0.1 on 2024-02-15 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_alter_buycart_amount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BuyCart',
            new_name='ShoppingCart',
        ),
    ]
