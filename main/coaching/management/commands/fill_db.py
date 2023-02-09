from django.core.management.base import BaseCommand
from coaching.models import Vacancy, File, Region
from data import regions, files

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for region in regions:
            Region.objects.create(id=region['id'], region=region['region'])
        for i, file in enumerate(files):
            File.objects.create(id=i, filename=file)
        
            Vacancy.objects.create(name="Pthon", region_id=3, file_id=i)