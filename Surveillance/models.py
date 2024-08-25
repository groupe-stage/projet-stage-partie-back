from django.db import models 
from Salle.models import Salle

class Surveillance(models.Model):
    id_surveillance = models.AutoField(primary_key=True)
    date_surveillance = models.DateField()
    id_salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date_surveillance)