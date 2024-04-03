from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    original_url = models.URLField()
    shortened_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shortened_url
