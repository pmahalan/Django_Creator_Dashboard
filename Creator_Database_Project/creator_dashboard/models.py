from django.db import models

# Create your models here.

class Creator(models.Model):
    name = models.CharField(max_length=200, null=True)
    upload = models.FileField(null=True)

