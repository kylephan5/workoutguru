from django.db import models

# Create your models here.


class MuscleGroups(models.Model):
    name = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.name


class Exercises(models.Model):
    musclegroup = models.ForeignKey(MuscleGroups, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    time = models.PositiveSmallIntegerField()
    image = models.ImageField(
        upload_to='media/', default='default.jpeg')
    reps = models.CharField(max_length=200)

    def __str__(self):
        return self.name
