from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ApplyLicence(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    FatherName = models.CharField(max_length=100,unique=True)
    NIDNumber=models.CharField(max_length=100,default="ovi")
    type = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    ward=models.CharField(max_length=100,default="ovi")
    pyment=models.CharField(max_length=100,default="ovi")

    def __str__(self):
        return str(self.name)

class HomeApplication(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    FatherName = models.CharField(max_length=100)
    wardno=models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    NIDNumber = models.CharField(max_length=100,unique=True)
    HondingNo=models.CharField(max_length=100)
    PreviousTax=models.CharField(max_length=100)
    SelectFloor=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='photo')
    payment=models.CharField(max_length=100)

    def  __str__(self):
        return str(self.name)


