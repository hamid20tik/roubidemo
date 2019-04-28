from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    BaseUserManager , AbstractBaseUser
    )

class UserMoshtari(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField(max_length=500)
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=14)
    def __str__(self):
        return f'{self.user.username}'


class UserMaghaze(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    code_meli = models.CharField(max_length=50)
    address = models.TextField(max_length=500)
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.user.username}'

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            usermaghaze = UserMaghaze.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile,sender=User)