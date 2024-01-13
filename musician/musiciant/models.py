from django.db import models

# Create your models here.

from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=50)

    CHOICES = {
        ('guitarac', "guitar"),
        ('flute', 'flute'),
        ('violin', 'violin'),
        ('drums', 'drum')

    }
    tools = models.CharField(max_length= 30 ,choices=CHOICES)

    academic_performance = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)]) #"ЭТО ПРОСТО ЧТО ТАКОЕ ЭТО ТАК ТРУДНО "
    status = models.BooleanField()

    def __str__(self):
        return f"{self.name}-{self.surname}"

    def get_absolut_url(self):
        return f"/check/{self.pk}"
