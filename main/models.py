from django.db import models

# Create your models here.


class Char(models.Model):
    name = models.CharField(max_length=32)
    person = models.CharField(max_length=32)
    race = models.CharField(max_length=32)
    clas = models.CharField(max_length=32)

    # Stats
    Melee = models.IntegerField()
    Range = models.IntegerField()
    WillPower = models.IntegerField()
    Strength = models.IntegerField()
    Agility = models.IntegerField()
    Intelligence = models.IntegerField()
    Toughness = models.IntegerField()
    Perception = models.IntegerField()
    Fellowship = models.IntegerField()
    FatePoints = models.IntegerField()

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=32, blank=False)