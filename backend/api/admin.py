from django.contrib import admin
from api.models.user import User
from api.models.course import Course
from api.models.enrollment import Enrollment
from api.models.lesson import Lesson
from api.models.quiz import Quiz
from api.models.progress import Progress
from api.models.domaine import Domaine

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'domaine', 'price')  # Ajout du prix dans l'affichage
    search_fields = ('title',)
    list_filter = ('domaine',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'price')  # Ajout du prix dans l'affichage
    search_fields = ('title',)
    list_filter = ('course',)

# Déclaration correcte de l'admin pour User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')  # Afficher ces champs
    list_filter = ('is_staff', 'is_superuser')  # Ajoute un filtre pour afficher les superutilisateurs

# Enregistrement des autres modèles
admin.site.register(Enrollment)
admin.site.register(Quiz)
admin.site.register(Progress)
admin.site.register(Domaine)
