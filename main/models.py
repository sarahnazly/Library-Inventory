from django.db import models

# Create your models here.
class Item(models.Model) :
    name = models.CharField(max_length=100)
    amount = models.IntegerField()  
    category = models.CharField(max_length = 50)
    borrow_date = models.DateField(null = True, blank = True)
    description = models.TextField()