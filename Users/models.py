from django.db import models
from Surveillance.models import Surveillance 
from Unite.models import Unite

class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    nom_user = models.CharField(max_length=100)
    prenom_user = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mdp = models.CharField(max_length=128)  # Pour stocker le mot de passe, vous devriez en fait utiliser un champ dédié pour les mots de passe, mais pour l'exemple, nous utilisons CharField
    cin = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    id_surveillance = models.ForeignKey(Surveillance, on_delete=models.CASCADE)
    identifiant = models.CharField(max_length=50)
    roleRes = models.CharField(max_length=50, blank=True, null=True)
    id_unite = models.ForeignKey(Unite, on_delete=models.CASCADE)
    image_user = models.ImageField(upload_to='user_images/', blank=True, null=True)
    

    def __str__(self):
        return self.nom_user
