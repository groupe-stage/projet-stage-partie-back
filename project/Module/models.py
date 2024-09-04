from django.db import models
from Niveau.models import Niveau

class Module(models.Model):
    id_module = models.AutoField(primary_key=True)
    nom_module = models.CharField(max_length=255)
    duree_module = models.IntegerField()
    id_niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)


    def __str__(self):
        return self.nom_module
