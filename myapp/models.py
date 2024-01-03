from django.db import models



from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    

class UserInfo(models.Model):

    username=models.CharField(max_length=40,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    
    