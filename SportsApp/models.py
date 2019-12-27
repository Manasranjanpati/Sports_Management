from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)






class SportsData(models.Model):

    sports_name = models.CharField(max_length=50)
    sports_type = models.CharField(max_length=50)
    sports_time = models.DateField(max_length=35)
    sports_coach = models.CharField(max_length=70)

    def __str__(self):
        return self.sports_name



class CustomerData(models.Model):

    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.BigIntegerField()

    Gender_Choices = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    gender = MultiSelectField(choices=Gender_Choices)


    SPRTS_CHOICES = (
        ('Kaba','Kabaddi'),
        ('Crick','Cricket'),    #I Used Multiselectfield here because i want to show multiple data...
        ('Volly','Vollyball'),
        ('Soccer','Soccer'),
        ('Basket','Basketball'),
        ('Base','Baseball'),
        ('Minton','Badminton'),
        ('Carrom','Carrom'),
        ('Swim','Swimming'),
        ('Chess','Chess'),
        ('Gym','Gymnastics'),
    )
    sports = MultiSelectField(max_length=25,choices=SPRTS_CHOICES)
    data_of_joining = models.DateField(max_length=100)

    def __str__(self):
        return self.name



