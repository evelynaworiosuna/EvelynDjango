from django.db import models

# Create your models here.

class Busines(models.Model):
    Category = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    BusinessName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    Password = models.CharField(max_length=50)
    Telephone = models.IntegerField()



    def __str__(self):
        return self.BusinessName
        

   