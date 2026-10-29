from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


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