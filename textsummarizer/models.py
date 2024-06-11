from django.db import models

class TextInput(models.Model):
    text = models.TextField()
    summary = models.TextField(blank=True)