from rest_framework import generics
from api.models.user import User 
from api.serializers.user_serializer import UserSerializer,  RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print("User ID:", user.id)
            user.is_active = False  # Empêche la connexion avant activation
            user.save()

            # Génération du lien d'activation
            current_site = get_current_site(request).domain
            activation_link = request.build_absolute_uri(reverse('activate-account', kwargs={'user_id': user.id}))


            # Envoi de l'email avec le lien
            send_mail(
                "Activation de votre compte",
                f"Merci de vous être inscrit. Veuillez activer votre compte en cliquant sur ce lien : {activation_link}",
                "devdelessard@gmail.com",
                [user.email],
                fail_silently=False,
            )

            return Response(
                {"message": "Compte créé avec succès. Veuillez activer votre compte par email.",
                 "user_id": user.id  # verification
                 },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        
        if user:
            if not user.is_active:
                return Response(
                    {"error": "Votre compte n'est pas activé. Veuillez l'activer par e-mail."},
                    status=status.HTTP_403_FORBIDDEN
                )
            
             # Supprime le token existant si nécessaire
            Token.objects.filter(user=user).delete()

            # Crée un nouveau token
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Identifiants incorrects"}, status=status.HTTP_400_BAD_REQUEST)

        

class ActivateUserView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if not user.is_active:
            user.is_active = True
            user.save()
            return Response({"message": "Compte activé avec succès"}, status=status.HTTP_200_OK)
        return Response({"message": "Ce compte est déjà activé"}, status=status.HTTP_400_BAD_REQUEST)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)