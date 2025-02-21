from django.db import models
from .lesson import Lesson

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question = models.TextField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question
