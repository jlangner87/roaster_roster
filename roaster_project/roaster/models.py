from unicodedata import category
from django.db import models

# Create your models here.

# User Model


class User(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    profile_pic = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

# Roaster Model


class Roaster(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="roaster")
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    site_url = models.CharField(max_length=200)
    display_pic = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

# Bean Model


class Bean(models.Model):
    roaster = models.ForeignKey(
        Roaster, on_delete=models.CASCADE, related_name="beans")
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    roast_type = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    buy_url = models.CharField(max_length=200)
    product_pic = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
