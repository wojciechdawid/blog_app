from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
    path("gallery/", views.GalleryList.as_view(), name="list"),
    path("gallery/<int:pk>", views.GalleryDetail.as_view(), name="gallery_detail"),
    path("gallery/<int:pk>/images/<int:picture_pk>", views.PictureDetail.as_view(), name="picture_detail")
]