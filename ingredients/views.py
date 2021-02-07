import json
from django.shortcuts import render

from rest_framework.views import APIView

# Create your views here.

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from ingredients.models import Ingredient, IngredientPurchaseDetail
from bakeryManagement.permissions import AdminAuthenticationPermission


class IngredientView(APIView):
    permission_classes = [AdminAuthenticationPermission]

    def get(self, request):
        ingredients = Ingredient.objects.all()
        return HttpResponse(ingredients.values())

    def post(self, request):
        ingredientName = request.data.get('ingredientName','')
        ingredientQuantity = request.data.get('ingredientQuantity','')
        purchasedFrom = request.data.get('purchasedFrom','')
        purchasedPrice = request.data.get('purchasedPrice',0)
        if not (ingredientName and ingredientQuantity):
            return HttpResponse(json.dumps({'result': False, 'message':'Name and quantity of ingredients are required'}))
        import pdb;pdb.set_trace()
        ing =  Ingredient.objects.filter(ingredientName=ingredientName)
        if ing:
            ing = ing[0]
        if ing:
            ing.ingredientQuantity+=int(ingredientQuantity)
        else:
            ing = Ingredient(ingredientName=ingredientName, ingredientQuantity=ingredientQuantity)
        ing.save()

        ingprice = IngredientPurchaseDetail(ingredientId = ing, purchasedFrom=purchasedFrom, purchasedPrice=purchasedPrice)
        ingprice.save()
        return HttpResponse(json.dumps({'result':True, 'message':'Ingredient details saved'}))
