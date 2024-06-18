from django.db import models

# Create your models here.
class House(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=4)
    image = models.ImageField(upload_to='houses/')
    
    def __str__(self):
        return self.title

class Apartment(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=4)
    image = models.ImageField(upload_to='apartments/')
    
    def __str__(self):
        return self.title

class Land(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=4)
    image = models.ImageField(upload_to='lands/')
    
    def __str__(self):
        return self.title
