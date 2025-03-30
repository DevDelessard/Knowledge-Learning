# api/views/achat.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models.achat import Achat
from api.serializers.achat_serializer import AchatSerializer

class AchatListCreateView(generics.ListCreateAPIView):
    serializer_class = AchatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 🧠 Ne retourne que les achats de l'utilisateur connecté
        return Achat.objects.filter(utilisateur=self.request.user)

    def perform_create(self, serializer):
        # 👤 Ajoute automatiquement l'utilisateur connecté
        serializer.save(utilisateur=self.request.user)
