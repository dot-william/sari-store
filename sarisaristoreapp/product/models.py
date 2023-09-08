from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=1000, decimal_places=2)
    expiration_date = models.DateField()
    
    def __str__(self):
        return self.name