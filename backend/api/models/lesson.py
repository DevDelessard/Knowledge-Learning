from django.db import models
from .course import Course

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="lessons")
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Ajout du prix


    @property
    def domaine(self):
        return self.course.domaine  # Récupère le domaine du cours

    def __str__(self):
        return self.title