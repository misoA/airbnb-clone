from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command delete rooms"

    def handle(self, *args, **options):
        rooms = room_models.Room.objects.all()
        rooms.delete()
        self.stdout.write(self.style.SUCCESS(f"Rooms deleted!"))
