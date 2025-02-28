from django.db import models
from .domaine import Domaine



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    domaine = models.ForeignKey(Domaine, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Ajout du prix



    def __str__(self):
        return self.title
