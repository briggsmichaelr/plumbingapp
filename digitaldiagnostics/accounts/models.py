from django.db import models
from django.contrib.auth.models import User

class Userinfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key = True)
    name = models.CharField(max_length = 500)
    #zip
    #address
    #city
    #state

# Create your models here.
