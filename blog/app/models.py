from django.db import models
from PIL import Image
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


class MediaLibrary(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Название (для поиска)")
    image = models.ImageField(upload_to='uploads/library/', verbose_name="Изображение")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Медиатека"
        verbose_name_plural = "Медиатека"

    def save(self, *args, **kwargs):
        # Сначала сохраняем файл на диск
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            
            if os.path.exists(img_path) and not img_path.endswith('.webp'):
                img = Image.open(img_path)
                
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Уменьшаем до 1600px
                if img.width > 1600:
                    output_size = (1600, int(img.height * (1600 / img.width)))
                    img = img.resize(output_size, Image.Resampling.LANCZOS)

                # Сохраняем как WebP (самый легкий формат)
                webp_path = img_path.rsplit('.', 1)[0] + '.webp'
                img.save(webp_path, 'WEBP', quality=85, optimize=True)

                # Удаляем оригинал
                os.remove(img_path)
                
                # Обновляем путь в БД
                self.image.name = self.image.name.rsplit('.', 1)[0] + '.webp'
                super().save(update_fields=['image'])

    def __str__(self):
        return self.title or f"Картинка {self.id}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    preimage = models.ImageField(upload_to='static/images/')
    prebody = models.TextField()
    body = models.TextField()


    class Meta:
        ordering = ['-published']


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.preimage:
            img_path = self.preimage.path
            if os.path.exists(img_path):
                if not img_path.endswith('.webp'):
                    img = Image.open(img_path)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    if img.width > 1600:
                        output_size = (1600, int(img.height * (1600 / img.width)))
                        img = img.resize(output_size, Image.Resampling.LANCZOS)
                    webp_path = img_path.rsplit('.', 1)[0] + '.webp'
                    img.save(webp_path, 'WEBP', quality=85, optimize=True)
                    os.remove(img_path)
                    self.preimage.name = self.preimage.name.rsplit('.', 1)[0] + '.webp'
                    super().save(update_fields=['preimage'])


    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


@receiver(post_save, sender=Post)
def send_new_post_notification(sender, instance, created, **kwargs):
    if created:
        subscribers = Subscriber.objects.all()
        emails = [sub.email for sub in subscribers]

        if emails:
            # URL нового поста
            post_url = f"https://blog.maylov.ru/app/post/{instance.id}/"

            message = (
                f"Новая статья опубликована: {instance.title}\n\n"
                f"{instance.prebody[:200]}...\n\n"
                f"Читать: {post_url}"
            )

            send_mail(
                subject=f"Новая статья: {instance.title}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=emails,
            )
