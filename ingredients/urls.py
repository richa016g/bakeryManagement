from django.urls import path
from ingredients import views


urlpatterns = [
    path('', views.IngredientView.as_view())
]