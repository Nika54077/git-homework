from django.urls import path
from .views import get_all_students, get_student,get_all_teachers, get_teacher, get_all_classes, get_class


urlpatterns = [
    path('students/', get_all_students, name='get_all_students'),
    path('students/<int:id>/', get_student, name='get_student'),

    path('teachers/', get_all_teachers, name='get_all_teachers'),
    path('teachers/<int:id>/', get_teacher, name='get_teacher'),

    path('classes/', get_all_classes, name='get_all_classes'),
    path('classes/<int:id>/', get_class, name='get_class'),
]
