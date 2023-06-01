from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    tel=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
   
    def __str__(self):
      return f"{self.first_name} {self.last_name}"