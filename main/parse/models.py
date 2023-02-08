from django.db import models

# Create your models here.

class Region(models.Model):
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