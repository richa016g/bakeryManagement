from django.db import models
import uuid
# Create your models here.

class Ingredient(models.Model):

    ingredientName = models.CharField(primary_key=True, max_length=100)
    ingredientQuantity = models.IntegerField()



class IngredientPurchaseDetail(models.Model):
    ingredientId = models.ForeignKey(Ingredient,default=uuid.uuid4(), on_delete=models.CASCADE)
    purchasedFrom = models.CharField(max_length=100)
    purchasedPrice = models.CharField(max_length=100)