from django.db import models
from django.contrib.auth.models import User



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

class HomeTax(models.Model):
    name= models.ForeignKey(User, on_delete=models.CASCADE)
    ward_no = models.CharField(max_length=100)
    HoldingNo=models.CharField(max_length=100)
    taxyear=models.CharField(max_length=100)
    TaxType=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    pictureowner=models.ImageField(upload_to='photo')
    payment=models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)



class Onlinebdapply(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    PersonalNumber=models.CharField(max_length=17,unique=True)
    FatherName = models.CharField(max_length=100)
    MotherName = models.CharField(max_length=100)
    BithofDate = models.CharField(max_length=100)
    PresentAddress = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    subdistict = models.CharField(max_length=100)
    oldpic = models.ImageField(upload_to='photo')

    def  __str__(self):
        return str(self.name)





class Addproblem(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    ProblemType=models.CharField(max_length=100)
    WardNo=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Breif=models.CharField(max_length=250)
    ProblemPicture=models.ImageField(upload_to='photo')

    def  __str__(self):
        return str(self.name)



class publicfeedback(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    throwby=models.CharField(max_length=250)
    throwby=models.CharField(max_length=250)
    description=models.CharField(max_length=250)

    def  __str__(self):
        return str(self.name)






