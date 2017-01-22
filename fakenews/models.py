from django.db import models

# Create your models here.

class Result(models.Model):
    url_hash = models.SlugField(max_length=32)
    url = models.TextField(null=True)
    is_real = models.BooleanField()
