from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates facilities"

    def handle(self, *args, **options):
        room_types = [
            "Shared room",
            "Hotel room",
            "Private room",
            "Entire place",
        ]
        for r in room_types:
            RoomType.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(room_types)} Facilities created!"))
