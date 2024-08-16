# Generated by Django 5.0.7 on 2024-08-13 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Surveillance', '0001_initial'),
        ('Unite', '0001_initial'),
        ('Users', '0003_appuser_delete_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='id_surveillance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Surveillance.surveillance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='id_unite',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Unite.unite'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='image_user',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]
