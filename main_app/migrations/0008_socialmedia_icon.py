# Generated by Django 5.0.1 on 2024-01-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_companies_slug_alter_products_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='icon',
            field=models.TextField(blank=True, null=True),
        ),
    ]
