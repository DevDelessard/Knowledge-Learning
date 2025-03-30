from django.urls import path
from api.views.course_views import CourseListView, CourseDetailView
from api.views.user_views import UserListView, UserDetailView, RegisterView, LoginView, ActivateUserView
from api.views.enrollment_views import EnrollmentListView, EnrollmentDetailView
from api.views import home  # Import pour la page d'accueil
from api.views.domaine_views import DomaineListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.achat import AchatListCreateView
from api.views.user_views import MeView
from api.views.lesson_views import ValiderLessonView, LessonDetailView
from api.views.course_views import CertificationsView

urlpatterns = [
    path('', home, name='home'),

    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('enrollments/', EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment-detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('domaines/', DomaineListView.as_view(), name='domaine-list'),
    

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name="login"),
    path('activate/<uidb64>/<token>/', ActivateUserView.as_view(), name='activate'),


    # Pour créer un achat
    path("achats/", AchatListCreateView.as_view(), name="achats"),

    # Pour récupérer les achats de l'utilisateur connecté
    
    path('users/me/', MeView.as_view(), name='user-me'),
    path("lessons/<int:pk>/", LessonDetailView.as_view(), name="lesson-detail"),
    path("lessons/<int:lesson_id>/valider/", ValiderLessonView.as_view(), name="valider-lecon"),

    path("certifications/", CertificationsView.as_view(), name="certifications"),




]
