from django.db import models

# Create your models here.
class Item(models.Model) :
    name = models.CharField(max_length=100)
    amount = models.IntegerField() 
    description = models.TextField() 
    category = models.CharField(max_length = 50)
    tanggal_peminjaman = models.DateField(null = True, blank = True)