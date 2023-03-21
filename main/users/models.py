from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    ADMIN = "ADMIN"
    STUDENT = "STUDENT"
    COACH = "COACH"
    ROLES = [
        (ADMIN, "Админ"),
        (STUDENT, "Ученик"),
        (COACH, "Тренер")
    ]

    email = models.EmailField(unique=True, verbose_name="E-mail")
    '#date_of_birth = models.DateTimeField(verbose_name="Дата рождения", null=True)'
    type = models.CharField(choices=ROLES, max_length=20)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'type']
    

"""class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Students"
        COACH = "COACH", "Coach"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class Student(User):

    base_role = User.Role.STUDENT

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for students"""