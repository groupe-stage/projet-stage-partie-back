# Generated by Django 4.2.5 on 2024-11-06 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bloc', '0001_initial'),
        ('Examen', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id_salle', models.AutoField(primary_key=True, serialize=False)),
                ('nom_salle', models.CharField(max_length=255)),
                ('capacite', models.IntegerField()),
                ('dispo', models.BooleanField(default=True)),
                ('id_bloc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloc.bloc')),
                ('id_examen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Examen.examen')),
            ],
        ),
    ]
