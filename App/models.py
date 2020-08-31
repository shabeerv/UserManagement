from django.db import models

# Create your models here.
class Product(models.Model):  
    p_id = models.IntegerField()  
    product_name = models.CharField(max_length=100)  
    category = models.CharField(max_length=100) 
    price = models.IntegerField()  

    class Meta:  
        db_table = "products"