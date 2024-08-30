from django.db import models
from Salle.models import Salle
from Examen.models import Examen

class Salle_examen(models.Model):
    id_salle = models.ForeignKey(Salle, on_delete=models.CASCADE, primary_key=True)
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    date_salle = models.DateField()
    def __str__(self):
        return f'{self.id_salle} - {self.id_examen}'
