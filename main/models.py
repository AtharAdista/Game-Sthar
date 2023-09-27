from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    data_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.TextField()
    platform = models.TextField()

