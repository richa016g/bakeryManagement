from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BakeryUser(User):
    ROLES = (

        ('admin', 'admin'),
        ('customer', 'customer'),

    )

    roles = models.CharField(max_length=50, choices = ROLES, null=True)

    def __str__(self):
        return self.username