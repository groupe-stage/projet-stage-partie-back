# Generated by Django 5.0.7 on 2024-08-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contrainte', '0007_alter_contrainte_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrainte',
            name='nom_contrainte',
            field=models.CharField(choices=[('enceinte', 'Enceinte'), ('congé', 'Congé'), ('congé de maladie', 'Congé de maladie'), ('état de santé', 'État de santé')], max_length=255),
        ),
    ]
