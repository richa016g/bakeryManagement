from django.contrib import admin
from ingredients.models import Ingredient, IngredientPurchaseDetail

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(IngredientPurchaseDetail)