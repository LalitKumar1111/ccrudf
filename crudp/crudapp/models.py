from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    email =models.EmailField(max_length = 50)
    address = models.TextField(max_length = 200)
