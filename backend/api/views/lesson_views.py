from rest_framework import generics
from api.models.lesson import Lesson
from api.serializers.lesson_serializer import LessonSerializer

class LessonByDomainView(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        domaine = self.kwargs['domaine']
        return Lesson.objects.filter(course__domaine=domaine)  # Filtrer par domaine
