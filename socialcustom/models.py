from django.db import models
from django.db.models import CharField
# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=128 , unique=False)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=10)
    # password2 = models.CharField(max_length=12)
