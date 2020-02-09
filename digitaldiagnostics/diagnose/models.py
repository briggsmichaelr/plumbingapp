from django.db import models


class Report(models.Model):
    room = models.CharField(max_length = 500, default = 'NA')
    where = models.CharField(max_length = 500, default = 'NA')
    #image = models.ImageField(upload_to = 'images/', null = True)
    time = models.DateField(auto_now_add=True)


    #def __str__(self):
        #return self.user
