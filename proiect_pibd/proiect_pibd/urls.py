from django.contrib import admin
from django.urls import path, include  # include trebuie să fie aici!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_project.urls')), # Asigură-te că numele aplicației e corect
]