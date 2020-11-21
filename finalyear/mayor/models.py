from django.db import models

class FileAdmin(models.Model):
    adminupload = models.FileField(upload_to='media')
    tittle=models.CharField(max_length=100)
    NIDNumber=models.CharField(max_length=100,unique=True)
    HondingNo = models.CharField(max_length=100)
    wardno = models.CharField(max_length=10)
    is_published = models.BooleanField()
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return str(self.tittle)

    class Meta:
        ordering = ('-list_date',)