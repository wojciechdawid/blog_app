import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
import random

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

    name = factory.Faker("sentence", nb_words=1)
    description = factory.Faker("text")


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=4)
    content = factory.Faker("text")
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    likes = factory.LazyFunction(lambda: random.randint(0, 1000))
