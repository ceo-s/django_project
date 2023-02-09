from django.core.management.base import BaseCommand
from coaching.models import Vacancy, File, Region

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        vacncies = Vacancy.objects.all()
        [print(vac) for vac in vacncies]

        files = File.objects.all()
        [print(file) for file in files]

        regions = Region.objects.all()
        [print(reg) for reg in regions]