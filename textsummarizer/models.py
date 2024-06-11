# summarizer/models.py

from django.db import models

class TextSummary(models.Model):
    text = models.TextField()
    summary = models.TextField()

    def __str__(self):
        return self.text[:50]  # Return the first 50 characters of the text
