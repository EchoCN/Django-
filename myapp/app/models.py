from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    race = models.CharField(max_length=20)

    def __str__(self):
        return self.name