from django.urls import path
from . import views

urlpatterns = [
    # Courses
    path('courses/', views.CourseListCreate.as_view()),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroy.as_view()),

    # Students
    path('students/', views.StudentListCreate.as_view()),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]