import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User

from.models import Post, Category


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker(90)
    description = factory.Faker.text(200)

