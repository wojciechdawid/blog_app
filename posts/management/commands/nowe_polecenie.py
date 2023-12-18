from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("n", type=int)

    def handle(self, *args, **options):
        for i in range(options.get("n", 0)):
            print("Hello World")
