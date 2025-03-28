# api/views/achat.py
from rest_framework import generics
from api.models.achat import Achat
from api.serializers.achat_serializer import AchatSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response



class AchatCreateView(generics.CreateAPIView):
    queryset = Achat.objects.all()
    serializer_class = AchatSerializer

class AchatListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        achats = Achat.objects.filter(utilisateur=user)
        serializer = AchatSerializer(achats, many=True)
        return Response(serializer.data)
