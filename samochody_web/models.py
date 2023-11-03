from django.db import models

# Create your models here.

class Car(models.Model):
    ENGINE_CHOICES = [
        ('benzyna', 'Benzyna'),
        ('diesel', 'Diesel'),
        ('hybryda', 'Hybryda'),
        ('elektryczny', 'Elektryczny'),
    ]

    DRIVE_TRAIN_CHOICES = [
        ('przednionapęd', 'Przedni napęd'),
        ('tylnionapęd', 'Tylni napęd'),
        ('napęd4x4', 'Napęd 4x4'),
    ]

    GEAR_CHOICES = [
        ('manulany', 'Manualny'),
        ('automatyczny', 'Automatyczny'),
    ]

    brand = models.CharField(max_length=16, blank=False)
    model = models.CharField(max_length=30, blank=False)
    year = models.PositiveSmallIntegerField(blank=False)
    engineCapacity = models.IntegerField(blank=False)
    engineType = models.CharField(max_length=16, choices=ENGINE_CHOICES, blank=False)
    gear = models.CharField(max_length=16, choices=GEAR_CHOICES, blank=False)
    drive_train = models.CharField(max_length=16, choices=DRIVE_TRAIN_CHOICES, blank=False)
    doors = models.IntegerField(blank=False)

def __str__(self):
    return self.brand + self.model