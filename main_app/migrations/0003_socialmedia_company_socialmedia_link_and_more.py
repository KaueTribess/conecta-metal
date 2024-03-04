# Generated by Django 5.0.1 on 2024-01-18 01:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_invoice_services_socialmedia_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.companies'),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='link',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='name',
            field=models.CharField(choices=[('WhatsApp', 'Whatsapp'), ('Instagram', 'Instagram'), ('Facebook', 'Facebook')], default='Instagram', max_length=9),
        ),
    ]
