from django.db import models


# Create your models here.
class Phones(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
