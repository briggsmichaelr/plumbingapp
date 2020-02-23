from django.db import models



class Report(models.Model):
    room = models.CharField(max_length = 500, default = 'NA')
    where = models.CharField(max_length = 500, default = 'NA')
    what = models.CharField(max_length = 500, default = 'NA')
    access = models.CharField(max_length = 500, default = 'NA')
    image = models.ImageField(upload_to = 'images/', default = 'images/Blank.png')
    when = models.CharField(max_length = 500, default = 'NA')
    damage = models.CharField(max_length = 500, default = 'NA')
    time = models.DateField(auto_now_add=True)
    user = models.CharField(max_length = 500, default = 'NA')


    #def __str__(self):
        #return self.user
