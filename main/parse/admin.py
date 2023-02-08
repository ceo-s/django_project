from django.contrib import admin
from .models import Vacancy, Region, File
# Register your models here.

admin.site.register(Vacancy)
admin.site.register(Region)
admin.site.register(File)