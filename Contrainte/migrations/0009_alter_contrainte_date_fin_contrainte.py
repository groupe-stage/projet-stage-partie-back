# Generated by Django 5.0.7 on 2024-09-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contrainte', '0008_alter_contrainte_nom_contrainte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrainte',
            name='date_fin_contrainte',
            field=models.DateTimeField(),
        ),
    ]
