from django.contrib import admin
from .models import Gallery, Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass


class PictureInline(admin.TabularInline):
    model = Picture
    extra = 3


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [PictureInline]


