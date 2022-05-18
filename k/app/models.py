from re import M
from django.db import models
from django.db import models
# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)
    desc=models.TextField()
    price=models.IntegerField()