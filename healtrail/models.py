from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    

    

def __str__(self):
        return f"{self.Product} is {self.product_name} long"
