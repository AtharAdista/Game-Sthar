from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    data_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.TextField()
    platform = models.TextField()


