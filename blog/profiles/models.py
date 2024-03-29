from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    avatar = models.ImageField("Аватар", upload_to='static/images/profiles/', blank=True, null=True)
    phone = models.CharField('Телефон', max_length=20)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50,  blank=True, null=True)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.seve()