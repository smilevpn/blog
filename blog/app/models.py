from django.db import models


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

    def __str__(self):
        return self.title
