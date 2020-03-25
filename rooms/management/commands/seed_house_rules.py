from django.core.management.base import BaseCommand
from rooms.models import HouseRule

class Command(BaseCommand):

    help = "This command creates facilities"

    def handle(self, *args, **options):
        house_rules = [
            "Pets allowed",
            "No Pets",
            "Smoking allowed",
            "No Smoking",
            "Not suitable for children and infants",
            "No parties or events",
        ]
        for h in house_rules:
            HouseRule.objects.create(name=h)
        self.stdout.write(self.style.SUCCESS(f"{len(house_rules)} Facilities created!"))
