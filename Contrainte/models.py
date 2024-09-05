from django.db import models
from Users.models import AppUser

class Contrainte(models.Model):
    id_contrainte = models.AutoField(primary_key=True)
    nom_contrainte = models.CharField(max_length=255)
    type_contrainte = models.CharField(max_length=255)
    date_debut_contrainte = models.DateField()
    date_fin_contrainte = models.DateField()
    status_contrainte = models.CharField(max_length=255)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_contrainte
