from django import forms
from django.contrib import admin
from .models import Post, MediaLibrary
from .models import Subscriber

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    body = forms.CharField(label="Полное описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    
@admin.register(MediaLibrary)
class MediaLibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'uploaded_at')
    search_fields = ('title',)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)
    ordering = ("-created_at",)

admin.site.register(Post, PostAdmin)

