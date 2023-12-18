from django.contrib.auth.models import User
from django.db import models


class TimestampedModel(models.Model):
    modified_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Post(TimestampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
