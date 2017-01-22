from django.db import models

# Create your models here.

class Result(models.Model):
    url_hash = models.SlugField(max_length=32)
    is_real = models.BooleanField()
