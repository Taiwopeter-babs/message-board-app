from django.db import models

# Create your models here.

class Post(models.Model):
    """Post class"""
    text = models.TextField(null=True)

    def __str__(self):
        return self.text[:50]