from django.db import models

# Create your models here.

class Timery(models.Model):

    def __str__(self):
        return  self.nazwa

    nazwa = models.CharField(max_length=100)
    date1 = models.TextField(blank=True)




