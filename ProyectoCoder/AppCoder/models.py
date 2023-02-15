from django.db import models

class Product(models.Model):
  title =models.CharField(max_length=50)
  code = models.IntegerField()
  price =models.CharField(max_length=50)
  stock =models.IntegerField()



class Client(models.Model):
    name = models.CharField(max_length=40)
    user = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField()


class Order(models.Model):
    number = models.IntegerField()
    products = models.CharField(max_length=40)
    address = models.CharField(max_length=40)


class Stores(models.Model):
    name = models.IntegerField()
    phone= models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    online = models.BooleanField()