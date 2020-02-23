from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Userinfo(models.Model):

    email = models.EmailField(max_length=254, default = 'NA', primary_key = True)

    phone = PhoneNumberField(default = '1234567890')

    name = models.CharField(max_length=1024, default = 'NA')

    address1 = models.CharField(max_length=1024, default = 'NA')

    address2 = models.CharField(max_length=1024, default = 'NA')

    zip_code = models.CharField(max_length=12, default = 'NA')

    city = models.CharField(max_length=1024, default = 'NA')

    state = models.CharField(max_length=1024, default = 'NA')

# Create your models here.
