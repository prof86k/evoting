from django.db import models

# Create your models here.

class PortFolio(models.Model):
    position = models.CharField("PortFolio",max_length=50,null=True)

class Candidate(models.Model):
    portfolio = models.ForeignKey(PortFolio,on_delete=models.CASCADE)
    name = models.CharField("Name:",max_length=50,null=True)
    image = models.ImageField(upload_to='Images/%d/%m/%Y',verbose_name='Image',null=True)
    logo = models.FileField(upload_to='Logos/%d/%m/%Y',null=True,verbose_name='Logo')
    vote = models.IntegerField(verbose_name='Vote',default=0)

    def __str__(self):
        return self.name

