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

class SiteUser(models.Model):
    name = models.TextField(null=True)
    age = models.IntegerField(null=True)
    experience = models.ForeignKey(to=TrainingExperience, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)

    class Meta:
        abstract = True


class Students(SiteUser):
    sport = models.ForeignKey(to=SportTag, on_delete=models.CASCADE, null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)

    def __str__(self) -> str:
        return f"{self.pk}"

class Coaches(SiteUser):
    sport = models.ForeignKey(to=SportTag, on_delete=models.CASCADE, null=True)
    coaching_experience = models.ForeignKey(to=CoachingExperience, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.name}"      

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
    #coach = models.ForeignKey(to=Coaches, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.pk}"