# Generated by Django 5.0.7 on 2024-07-23 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Niveau', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id_classe', models.AutoField(primary_key=True, serialize=False)),
                ('NbEtudiantClasse', models.IntegerField()),
                ('libelleClasse', models.CharField(max_length=255)),
                ('id_niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Niveau.niveau')),
            ],
        ),
    ]