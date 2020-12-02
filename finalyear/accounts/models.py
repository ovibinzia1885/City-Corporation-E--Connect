from django.db import models

class Others(models.Model):
    title=models.CharField(max_length=250)
    marque=models.CharField(max_length=200)
    photo_mayor = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_ceo = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_slider1 = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_slider2 = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_slider3 = models.ImageField(upload_to='photos/%y/%m/%d')
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-list_date',)

class School(models.Model):
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
    list=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    total_student=models.CharField(max_length=250)
    total_teacher=models.CharField(max_length=250)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.name
class FamousPlace(models.Model):
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
    placename=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    enviroment=models.CharField(max_length=250)
    closeday=models.CharField(max_length=250)

    def  __str__(self):
        return self.placename
class hotline(models.Model):
    THana=models.CharField(max_length=100)
    GovtHOspital=models.CharField(max_length=100)
    Firerservice=models.CharField(max_length=100)
    Bus_counter=models.CharField(max_length=100)
    Train_counter=models.CharField(max_length=100)

    def  __str__(self):
        return self.Bus_counter


class recentlysolveproblem(models.Model):
    title=models.CharField(max_length=250)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
    applicatename=models.CharField(max_length=250)
    wardno=models.CharField(max_length=20)
    type=models.CharField(max_length=250)
    location=models.CharField(max_length=250)

    def  __str__(self):
        return self.title

class councilorinfromation(models.Model):
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
    name=models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    wardno=models.CharField(max_length=20)
    phonnumber=models.CharField(max_length=250)

    def  __str__(self):
        return str(self.name)