from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from posts.models import Post, Category
from .forms import PostForm


def home_page(request):
    return render(
        request,
        "posts/home.html",
        {}
    )


class HomePageView(TemplateView):
    template_name = "posts/home.html"


def list_posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "posts/post_list.html",
        {"posts": page_obj}
    )


class PostList(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"
    paginate_by = 3


def post_details(request, pk: int):
    post = get_object_or_404(Post, pk=pk)
    return render(
        request,
        "posts/post_detail.html",
        {"object": post}
    )


class PostDetails(DetailView):
    model = Post


def add_post(request):
    if request.method == 'POST':
        title = request.POST.get("title"),
        content = request.POST.get("content")
        Post.objects.create(
            title=title,
            content=content,
            user=request.user,
        )
        return redirect("posts:list")
    return render(
        request,
        "posts/post_form.html",
        {}
    )


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    form = PostForm()
    return render(
        request,
        "posts/post_form.html",
        {"form": form}
    )


class PostAdd(CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoriesList(ListView):
    model = Category
    paginate_by = 10


class CategoryCreate(CreateView):
    model = Category
    fields = ["name", "description"]

