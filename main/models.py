from django.db import models

# Create your models here.


class MuscleGroups(models.Model):
    name = models.CharField(max_length=200)
    complete = models.BooleanField()
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class Exercises(models.Model):
    email = models.EmailField(null=True, blank=True)
    musclegroup = models.ForeignKey(MuscleGroups, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    time = models.PositiveSmallIntegerField()
    image = models.ImageField(
        upload_to='media/', default='default.jpeg')
    reps = models.CharField(max_length=200)
    selected = models.BooleanField()

    def __str__(self):
        return self.name
