from django.db import models
from django.contrib.auth.models import User
# from accounts.models import BakeryUser
from bakeryitem.models import BakeryItem
# Create your models here.

class OrderDetail(models.Model):
    customerId = models.ForeignKey(User, on_delete=models.CASCADE)
    itemPurchased = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchasedAt = models.FloatField()
    billerName = models.CharField(max_length=100)
    billedAddress = models.TextField()