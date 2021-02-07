import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from bakeryitem.models import BakeryItem
from bakeryManagement.permissions import AdminAuthenticationPermission

# Create your views here.

class BakeryItemCustomerView(APIView):

    permission_classes=[IsAuthenticated]

    def get(self, request):
        objs = BakeryItem.objects.values('itemName', 'containsEgg', 'sellingPrice')
        return HttpResponse(objs.values())

class BakeryItemView(APIView):
    permission_classes = [AdminAuthenticationPermission]

    def get(self, request):
        ingredients = BakeryItem.objects.all()
        return HttpResponse(ingredients.values())

    def post(self, request):
        itemName = request.data.get('itemName','')
        containsEgg = request.data.get('containsEgg','false') != 'false'
        costPrice = request.data.get('costPrice','')
        sellingPrice = request.data.get('sellingPrice','')
        quantity = request.data.get('quantity')
        if not (costPrice and sellingPrice and itemName):
            return HttpResponse(json.dumps({'result': False, 'message':'ItemName, CostPrice and SellingPrice are required'}))
    
        
        bakeryItem = BakeryItem(itemName=itemName,containsEgg=containsEgg, quantity=quantity, costPrice=costPrice, sellingPrice=sellingPrice)
        bakeryItem.save()

        return HttpResponse(json.dumps({'result':True, 'message':'Ingredient details saved'}))


    def put(self, request):
        bakeryItems = bakeryItems.objects.filter(itemName=itemName)
        if bakeryItems:
            bakeryItem = bakeryItems[0]
        else:
            return HttpResponse(json.dumps({'result':False, 'message':'Bakery Item not present'}))

        quantity = request.data.get('quantity',0)
        if quantity:
            bakeryItem.quantity += int(quantity)
        
        costPrice = request.data.get('costPrice')
        if costPrice:
            bakeryItem.costPrice = costPrice

        sellingPrice = request.data.get('sellingPrice')
        if sellingPrice:
            bakeryItem.sellingPrice = sellingPrice

        bakeryItem.save()
        return HttpResponse(json.dumps({'result': True, 'message':'Bakery Item details are updated'}))