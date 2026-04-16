from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path('courses/', views.CourseListCreate.as_view()),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroy.as_view()),

    path('students/', views.StudentListCreate.as_view()),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]