# Generated by Django 5.0.1 on 2024-02-22 11:46

import django.db.models.deletion
import utils.models_utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0029_alter_companies_profilepic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='concluded',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='requests',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='/main/default/no_profile_picture.png', null=True, upload_to=utils.models_utils.profile_image_upload),
        ),
    ]
