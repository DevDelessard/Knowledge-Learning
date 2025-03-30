from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from api.models.course import Course


User = get_user_model()

class InscriptionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = "/api/register/"
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }

    def test_inscription_reussie(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get(username="testuser")
        self.assertFalse(user.is_active)  # l'utilisateur n'est pas actif avant validation email


class ActivationCompteTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123"
        )
        self.user.is_active = False
        self.user.save()

        self.uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = default_token_generator.make_token(self.user)
        self.activation_url = f"/api/activate/{self.uid}/{self.token}/"

    def test_activation_compte(self):
        response = self.client.get(self.activation_url)
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_active)

class ConnexionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123"
        )
        self.user.is_active = False
        self.user.save()


    def test_connexion_reussie(self):
        response = self.client.post("/api/login/", {
            "username": "loginuser",
            "password": "mypassword"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)


class AchatTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="buyer", password="testpass")
        self.user.is_active = True
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(title="Cours Test", price=10.00)
        self.url = "/api/achats/create/"

    def test_achat_cursus(self):
        response = self.client.post(self.url, {
            "type_achat": "course",
            "course": self.course.id
        })
        self.assertEqual(response.status_code, 201)