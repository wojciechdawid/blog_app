from django.db import models
from posts.models import TimestampedModel


class Gallery(TimestampedModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Picture(TimestampedModel):
    img = models.ImageField(upload_to="gallery/%Y/%m/%d")
    text = models.CharField(max_length=200)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

