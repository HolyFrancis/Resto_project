from django.db import models

class Menu(models.Model):
    title=models.CharField( max_length=50, null=True)
    description=models.CharField(max_length=50, null=True)
    image=models.ImageField()
    status=models.BooleanField()
    
    def __str__(self):
        return self.title
    
    