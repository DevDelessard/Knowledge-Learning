from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Bienvenue sur Knowledge Learning API !"})

# Importation des autres vues
from .course_views import *
from .enrollment_views import *
from .user_views import *

