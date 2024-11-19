from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend_ionic.urls')),  # Conectar las rutas de la API
]
