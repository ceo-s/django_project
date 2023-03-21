from django.contrib import admin
from . import models
from django.db.models import QuerySet
# Register your models here.

admin.site.register(models.TrainingExperience)
admin.site.register(models.CoachingExperience)
admin.site.register(models.SportTag)
admin.site.register(models.Coaches)
admin.site.register(models.Students)
admin.site.register(models.CoachPosts)

def set_active(modeladmin, request, queryset: QuerySet):
    queryset.update(Active=True)
    pass

class ClientRequestAdmin(admin.ModelAdmin):
    # list_display = ["name", "age", "sport", "display"]
    actions = [set_active]
    

admin.site.register(models.ClientRequest, ClientRequestAdmin)
