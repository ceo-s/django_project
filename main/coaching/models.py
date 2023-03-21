from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User




class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Active=True)
    
class ActiveFieldMixin(models.Model):
    active = models.BooleanField(name="Active", default=True)
    objects = models.Manager()
    active_objects = ActiveManager()
    class Meta:
        abstract = True

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
    # email = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
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
    
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, **kwargs):
#     print("Сработал обработчик сигнала.")
#     if not Students.objects.filter(email=instance).exists():
#         Students.objects.create(email=instance)

class Coaches(SiteUser):
    sport = models.ForeignKey(to=SportTag, on_delete=models.CASCADE, null=True)
    coaching_experience = models.ForeignKey(to=CoachingExperience, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.name}"      

class ClientRequest(ActiveFieldMixin):
    name = models.TextField()
    age = models.IntegerField()
    sport = models.ForeignKey(to=SportTag, on_delete=models.CASCADE)
    experience = models.ForeignKey(to=TrainingExperience, on_delete=models.CASCADE)
    request = models.TextField()

    def __str__(self) -> str:
        return f"{self.pk}"

class CoachPosts(ActiveFieldMixin):
    sport = models.ForeignKey(to=SportTag, on_delete=models.CASCADE)
    #coach = models.ForeignKey(to=Coaches, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.pk}"
    
