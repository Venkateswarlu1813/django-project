from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home),

    # API routes
    path('api/', include('myapp.urls')),   # 👈 IMPORTANT
]