from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(default=0)  
    category = models.CharField(max_length = 50)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()
    