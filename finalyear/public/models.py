from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ApplyLicence(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    FatherName = models.CharField(max_length=100)
    NIDNumber=models.CharField(max_length=100,default="ovi")
    type = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    ward=models.CharField(max_length=100,default="ovi")
    pyment=models.CharField(max_length=100,default="ovi")

    def __str__(self):
        return str(self.name)

