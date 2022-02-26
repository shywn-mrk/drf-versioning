from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
