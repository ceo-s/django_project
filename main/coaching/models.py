from django.db import models

# Create your models here.



    


class TrainingExperience(models.Model):
    range = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.description}"
class CoachingExperience(models.Model):
    range = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.description}"
class SportTag(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"
class User():
    name = models.TextField()
    age = models.IntegerField()
    experience = models.ForeignKey(to=TrainingExperience, on_delete=models.CASCADE)

class Coaches(User, models.Model):
    sport = models.ForeignKey(to=SportTag, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.pk}"
class Students(User, models.Model):
    sport = models.ForeignKey(to=SportTag, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.pk}"
class ClientRequest(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    sport = models.ForeignKey(to=SportTag, on_delete=models.CASCADE)
    experience = models.ForeignKey(to=TrainingExperience, on_delete=models.CASCADE)
    request = models.TextField()

    def __str__(self) -> str:
        return f"{self.pk}"

"""class Region(models.Model):
    region = models.TextField()

    def __str__(self) -> str:
        return f"{self.pk}-{self.region}"

class File(models.Model):
    filename = models.TextField()

    def __str__(self) -> str:
        return f"{self.pk}-{self.filename}"

class Vacancy(models.Model):
    name = models.CharField(max_length=100, unique=False)
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE)
    file = models.ForeignKey(to=File, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.pk}-{self.name}"
"""
