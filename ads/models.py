from django.db import models

class Ad(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    height = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)

class AdImage(models.Model):
    ad = models.ForeignKey(Ad, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ads/')
