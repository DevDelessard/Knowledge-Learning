from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from api.models.lesson import Lesson
from api.serializers.lesson_serializer import LessonSerializer


class ValiderLessonView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, lesson_id):
        try:
            lesson = Lesson.objects.select_related('course').get(id=lesson_id)
            user = request.user
            lesson.validated_users.add(user)  # Étape 1 : valider la leçon

            # Étape 2 : vérifier les autres leçons du cursus
            course = lesson.course
            all_lessons = course.lessons.all()  # ✅ CORRECTION ICI

            if all(lesson.validated_users.filter(id=user.id).exists() for lesson in all_lessons):
                course.validated_users.add(user)  # Étape 3 : valider le cursus
                return Response({'message': '✅ Leçon et cursus validés avec succès.'}, status=status.HTTP_200_OK)

            return Response({'message': '✅ Leçon validée avec succès.'}, status=status.HTTP_200_OK)

        except Lesson.DoesNotExist:
            return Response({'error': '❌ Leçon introuvable.'}, status=status.HTTP_404_NOT_FOUND)



class LessonDetailView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
