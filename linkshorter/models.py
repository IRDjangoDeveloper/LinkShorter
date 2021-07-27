from django.db import models

# Create your models here.
class links(models.Model):
    link = models.URLField()
    short = models.CharField(max_length=100, unique=True)