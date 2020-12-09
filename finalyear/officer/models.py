from django.db import models


class Workshop(models.Model):
    tittle=models.CharField(max_length=120)
    type=models.CharField(max_length=120)
    duriation=models.CharField(max_length=120)
    Endclasstclass=models.CharField(max_length=120)
    perclass=models.CharField(max_length=120,verbose_name='perclassDuriation')
    is_published = models.BooleanField()
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
    startclass=models.CharField(max_length=120,)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.tittle

    class Meta:
        ordering = ('-list_date',)

class uploadbudget(models.Model):
    tittle=models.CharField(max_length=250)
    description=models.CharField(max_length=1000)
    photo=models.ImageField(upload_to='photo')

    def  __str__(self):
        return self.tittle

class FileAdmin(models.Model):
    adminupload = models.FileField(upload_to='media')
    tittle=models.CharField(max_length=100)
    FatherName=models.CharField(max_length=100)
    NIDNumber=models.CharField(max_length=100,unique=True)
    type = models.CharField(max_length=100)
    address = models.CharField(max_length=10)
    is_published = models.BooleanField()
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return str(self.tittle)

    class Meta:
        ordering = ('-list_date',)


class OnlineBd(models.Model):
    document = models.FileField(upload_to='media')
    PersonalNumber = models.CharField(max_length=17, unique=True)
    BithofDate = models.CharField(max_length=100)
    is_published = models.BooleanField()
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.PersonalNumber)

    class Meta:
        ordering = ('-list_date',)

class smsmayor(models.Model):
    subject=models.CharField(max_length=250)
    description=models.CharField(max_length=360)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.subject

class notice(models.Model):
    title=models.CharField(max_length=250)
    date=models.DateField()
    is_published = models.BooleanField()
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.title



