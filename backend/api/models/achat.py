from django.db import models
from django.contrib.auth import get_user_model
from .course import Course
from .lesson import Lesson

class Achat(models.Model):
    ACHAT_CHOICES = (
        ('course', 'Cours'),
        ('lesson', 'Leçon'),
    )

    utilisateur = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='achats')
    type_achat = models.CharField(max_length=10, choices=ACHAT_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    date_achat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.type_achat == 'course':
            return f"{self.utilisateur.username} a acheté le cours : {self.course}"
        else:
            return f"{self.utilisateur.username} a acheté la leçon : {self.lesson}"
