
from django.urls import path
from bakeryitem import views

urlpatterns = [
    path('', views.BakeryItemView.as_view()),
    path('customer', views.BakeryItemCustomerView.as_view())
]