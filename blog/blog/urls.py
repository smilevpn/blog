"""
URL configuration for blog project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

from app import views as app_views

urlpatterns = [
    # --- СТАТИКА И МЕДИА В САМОМ НАЧАЛЕ ---
    # Используем re_path и serve, чтобы отдавать файлы даже при DEBUG = False
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # --- ВАШИ ОСТАЛЬНЫЕ МАРШРУТЫ ---
    path('', app_views.BlogListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('app/', include('app.urls')),
    path('profile/', include('profiles.urls')),
]
