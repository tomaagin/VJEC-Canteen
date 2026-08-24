from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class StockItem(models.Model):
    item_name = models.CharField(max_length = 100)
    category = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
    def __str__(self):
        return self.item_name