
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoas/', include('apps.pessoa.urls')),
    path('', include('apps.pessoa.urls')),
]
