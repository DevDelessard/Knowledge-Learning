from rest_framework import serializers
from api.models.lesson import Lesson

class LessonSerializer(serializers.ModelSerializer):
    domaine = serializers.CharField(source='domaine', read_only=True)  # Ajoute le domaine

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'course', 'domaine']  # Ajoute le champ domaine
