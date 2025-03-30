from rest_framework import serializers
from api.models.lesson import Lesson

class LessonSerializer(serializers.ModelSerializer):
    domaine = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'course', 'domaine']

    def get_domaine(self, obj):
        return obj.domaine  # Cela appelle le @property du modèle Lesson
