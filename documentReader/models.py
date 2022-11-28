from django.db import models

class Reader(models.Model):
    type= models.CharField(max_length=1)
    date= models.CharField(max_length=6)
    value= models.CharField(max_length=10)
    cpf= models.CharField(max_length=11)
    card= models.CharField(max_length=15)
    hour= models.CharField(max_length=6)
    owner= models.CharField(max_length=50)
    store= models.CharField(max_length=150)
