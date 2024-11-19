from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    gender=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.name