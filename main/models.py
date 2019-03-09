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
    Perception = models.IntegerField()
    Toughness = models.IntegerField()
    Fellowship = models.IntegerField()
    FatePoints = models.IntegerField()

    Melee_bonus = models.IntegerField(default=0)
    Range_bonus = models.IntegerField(default=0)
    WillPower_bonus = models.IntegerField(default=0)
    Strength_bonus = models.IntegerField(default=0)
    Agility_bonus = models.IntegerField(default=0)
    Intelligence_bonus = models.IntegerField(default=0)
    Perception_bonus = models.IntegerField(default=0)
    Toughness_bonus = models.IntegerField(default=0)
    Fellowship_bonus = models.IntegerField(default=0)
    CurrentFP = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=32, blank=False)
