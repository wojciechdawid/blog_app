from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy, reverse


class TimestampedModel(models.Model):
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse_lazy("posts:categories")


class Post(TimestampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:details", kwargs={"pk": self.pk})
