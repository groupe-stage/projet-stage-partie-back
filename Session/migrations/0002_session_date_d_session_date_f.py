# Generated by Django 5.0.7 on 2024-09-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='date_d',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='session',
            name='date_f',
            field=models.DateField(default='2024-01-02'),
        ),
    ]
