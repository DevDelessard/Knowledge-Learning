from django.db import models
from django.contrib.auth.models import User  # 👈 à ajouter
from .domaine import Domaine
from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    domaine = models.ForeignKey(Domaine, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    # ✅ Ajout de ce champ pour suivre les cursus validés par utilisateur
    validated_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="validated_courses")

    def __str__(self):
        return self.title
