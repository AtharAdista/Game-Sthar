from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    data_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.TextField()
    platform = models.TextField()


