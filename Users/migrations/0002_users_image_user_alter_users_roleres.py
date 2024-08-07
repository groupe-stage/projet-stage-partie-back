# Generated by Django 5.0.7 on 2024-07-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image_user',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
        migrations.AlterField(
            model_name='users',
            name='roleRes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
