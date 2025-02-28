from django.db import models

class Domaine(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom
