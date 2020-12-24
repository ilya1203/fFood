from django.db import models



class Restoraunts(models.Model):

    name = models.TextField()
    long = models.TextField()
    width = models.TextField()

    class Meta:
        verbose_name_plural = 'Restourants'
        verbose_name = 'Restorant'