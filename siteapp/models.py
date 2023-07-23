from django.db import models

# Create your models here.
class contactInformation(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    pnumber = models.IntegerField()
    email = models.EmailField(max_length=120)
    subject = models.TextField(max_length=500)

    def __str__(self):
        return (self.fname)
    
