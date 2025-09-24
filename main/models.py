from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)                
    price = models.IntegerField()                         
    description = models.TextField()                       
    thumbnail = models.URLField()                        
    category = models.CharField(max_length=50)            
    is_featured = models.BooleanField(default=False)       
    quantity = models.IntegerField(default=0)             
    brand = models.CharField(max_length=50, default="")    

    def __str__(self):
        return self.name
