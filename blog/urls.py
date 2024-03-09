from django.contrib import admin
from django.urls import path, include  # новое изменение

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include("profiles.urls")),
    path('', include('blog.urls')),
]

