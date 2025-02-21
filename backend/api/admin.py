from django.contrib import admin
from api.models.user import User
from api.models.course import Course
from api.models.enrollment import Enrollment
from api.models.lesson import Lesson
from api.models.quiz import Quiz
from api.models.progress import Progress






admin.site.register(User)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Progress)

