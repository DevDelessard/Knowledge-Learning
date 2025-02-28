from rest_framework import generics
from api.models.domaine import Domaine
from api.serializers.domaine_serializer import DomaineSerializer

class DomaineListView(generics.ListAPIView):
    queryset = Domaine.objects.all()
    serializer_class = DomaineSerializer
