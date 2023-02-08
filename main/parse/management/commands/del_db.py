from django.core.management.base import BaseCommand
from parse.models import Vacancy, File, Region

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Region.objects.all().delete()
        File.objects.all().delete()
        Vacancy.objects.all().delete()