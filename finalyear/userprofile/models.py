from django.db import models
from django.contrib.auth.models import User
from django.db import models

class UserRole(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=20)
class Officer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    wardno=models.CharField(max_length=10)

