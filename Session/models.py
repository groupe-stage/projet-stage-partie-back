from django.db import models

class Session(models.Model):
    id_session = models.AutoField(primary_key=True)
    nom_session = models.CharField(max_length=255)
    type_session = models.CharField(max_length=255)


    def __str__(self):
        return self.nom_session
