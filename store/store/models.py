from django.db import models

class ProductModel(models.Model):
    Image = models.CharField(max_length=250)
    Name = models.CharField(max_length=250)
    Price = models.FloatField()
    Desc = models.CharField(max_length=250)
    