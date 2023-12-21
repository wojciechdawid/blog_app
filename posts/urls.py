from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = "posts"

urlpatterns = [
    # path("", views.home_page, name="home"),
    # path("", TemplateView.as_view(template_name="posts/home.html")),
    path("", views.HomePageView.as_view(), name="home"),
    # path("posts/", views.list_posts, name="list"),
    path("posts/", views.PostList.as_view(), name="list"),
    # path("posts/<int:id>/", views.post_details, name="details"),
    path("posts/<int:pk>/", views.PostDetails.as_view(), name="details"),
    # path("posts/add/", views.add_post, name="add"),
    # path("posts/add/", views.create_post, name="add"),
    path("posts/add/", views.PostAdd.as_view(), name="add"),

    path("categories/", views.CategoriesList.as_view(), name="categories"),
    path("categories/add", views.CategoryCreate.as_view(), name="create-category"),
    path("myview/", views.my_view, name="translation_example")
]
