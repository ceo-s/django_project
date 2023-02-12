from django.db import models


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
class User(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    experience = models.ForeignKey(to=TrainingExperience, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Coaches(User):
    sport = models.ForeignKey(to=SportTag, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.pk}"
class Students(User):
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

class CoachPosts(models.Model):
    sport = models.ForeignKey(to=SportTag, on_delete=models.CASCADE)
    coach = models.ForeignKey(to=Coaches, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.pk}"