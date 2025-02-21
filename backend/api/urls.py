from django.urls import path
from api.views.course_views import CourseListView, CourseDetailView
from api.views.user_views import UserListView, UserDetailView
from api.views.enrollment_views import EnrollmentListView, EnrollmentDetailView
from api.views import home  # Import pour la page d'accueil

urlpatterns = [
    path('', home, name='home'),  # Page d'accueil de l'API

    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('enrollments/', EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment-detail'),

]