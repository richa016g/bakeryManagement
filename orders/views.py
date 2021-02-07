import json
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from bakeryitem.models import BakeryItem
from orders.models import OrderDetail

class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        ordersPlaced = OrderDetail.objects.filter(customerId=request.user)
        return HttpResponse(ordersPlaced.values())

    def post(self, request):
        import pdb;pdb.set_trace()
        itemName = request.data.get('itemName')
        quantity = int(request.data.get('quantity',0))
        try:
            itemDetails = BakeryItem.objects.filter(itemName=itemName)[0]
        except:
            return HttpResponse(json.dumps({'result':False, 'message': f'Item {itemName} not present in database'}))
        if quantity <=0:
            return HttpResponse(json.dumps({'result':False, 'message': f'Quanity should be greater than 0'}))
        purchasedAt = itemDetails.sellingPrice * quantity
        billerName = request.data.get('billerName')
        billedAddress = request.data.get('billedAddress')

        orderdetail = OrderDetail(customerId=request.user, itemPurchased=itemDetails, purchasedAt=purchasedAt,
                                    billerName=billerName, billedAddress=billedAddress, quantity=quantity)
        orderdetail.save()

        itemDetails.quantity -= int(quantity)
        itemDetails.save()
        return HttpResponse(json.dumps({'result':True, 'message': 'Order placed successfully'}))




