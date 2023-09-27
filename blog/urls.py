from django.contrib import admin
from django.urls import path, include
from . import views as core_views
 
urlpatterns = [
    path('', core_vievs.index, name='index'),
    path('admin/', admin.site.urls),
    path('app/', include("app.urls")),
]

