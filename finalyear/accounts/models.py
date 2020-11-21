from django.db import models

class Others(models.Model):
    tittle=models.CharField(max_length=250)
    marque=models.CharField(max_length=200)
    photo_mayor = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_ceo = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_slider1 = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_slider2 = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_slider3 = models.ImageField(upload_to='photos/%y/%m/%d')
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-list_date',)

