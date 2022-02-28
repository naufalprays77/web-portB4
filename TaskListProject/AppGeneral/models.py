from pyexpat import model
from django.db import models

# Create your models here.

class Status(models.Model):
    strStatus       = models.TextField(max_length=30)
    strnotes        = models.TextField(max_length=100)
    
    def __str__(self):
        return self.strStatus
    
class Priorty(models.Model):
    strPriorty      = models.TextField(max_length=30)
    strnotes        = models.TextField(max_length=100)
    
    def __str__(self):
        return self.strPriorty