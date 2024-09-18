from django.db import models

# Create your models here.

class Cars(models.Model):
    name=models.CharField(max_length=200)
    content=models.TextField()
    brend=models.CharField(max_length=50)
    created_ad=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name





