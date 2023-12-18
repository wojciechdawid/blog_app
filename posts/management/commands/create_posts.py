from django.core.management.base import BaseCommand, CommandParser
from faker import Faker
from typing import Any

from posts.models import Post

faker = Faker("pl_PL")


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("n", type=int)

    def handle(self, *args: Any, **options: Any) -> str | None:
        n = options.get("n", 0)
        for i in range(n):
            Post.objects.create(
                title=faker.sentence(4),
                content=faker.paragraph(1),
                user_id=1
            )
        print(f"Utworzono {n} postów.")