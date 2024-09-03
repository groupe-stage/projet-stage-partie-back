# Generated by Django 5.0.6 on 2024-09-02 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Module', '0001_initial'),
        ('Niveau', '0002_alter_niveau_specialite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module_niveau',
            fields=[
                ('idmn', models.AutoField(primary_key=True, serialize=False)),
                ('id_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_niveaux', to='Module.module')),
                ('id_niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_niveaux', to='Niveau.niveau')),
            ],
        ),
    ]