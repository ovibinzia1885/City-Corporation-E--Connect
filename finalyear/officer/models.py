from django.db import models


class Workshop(models.Model):
    tittle=models.CharField(max_length=120)
    type=models.CharField(max_length=120)
    duriation=models.CharField(max_length=120)
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
