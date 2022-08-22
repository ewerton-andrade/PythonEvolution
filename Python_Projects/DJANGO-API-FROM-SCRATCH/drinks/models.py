## Here we construct the models of the data we want to send

from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=200) #Drink name data
    description = models.CharField(max_length=500) #Drink desdription data

    def __str__(self):
        return self.name

