from django.db import models
#creating models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

