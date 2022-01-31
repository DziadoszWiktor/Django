#importing money field (pip install django-money)
from djmoney.models.fields import MoneyField
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='PLN',
        max_digits=10,
    )
    summary = models.TextField(default='default value')