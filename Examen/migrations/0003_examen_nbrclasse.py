# Generated by Django 5.0.7 on 2024-09-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examen', '0002_remove_examen_date_examen'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='nbrclasse',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
