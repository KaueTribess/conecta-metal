# Generated by Django 5.0.1 on 2024-02-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_rename_buycart_shoppingcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='finalPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]
