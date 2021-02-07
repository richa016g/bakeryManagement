from django.db import models

# Create your models here.

class BakeryItem(models.Model):

    from_ingrdients = models.TextField() 
    # This will contain a json string with ingredient : percentage key value pairs
    itemName = models.CharField(max_length=100)
    containsEgg = models.BooleanField(default=False)
    costPrice = models.FloatField()
    sellingPrice = models.FloatField()
    quantity = models.IntegerField()
