from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50,primary_key=True)
    email=models.CharField(max_length=50,default="")
    address1=models.CharField(max_length=50,default="")
    address2=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=50,default="")
    phoneno=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name
