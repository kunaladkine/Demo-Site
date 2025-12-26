from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
