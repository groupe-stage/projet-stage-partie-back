# Generated by Django 5.0.7 on 2024-08-13 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contrainte', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrainte',
            name='id_user',
        ),
    ]
