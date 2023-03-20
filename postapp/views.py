from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Post
from django.views.generic import ListView, DetailView, CreateView

from django.views.generic.edit import DeleteView, UpdateView


# Create your views here.

class PostCreateView(CreateView):
    model = Post
    template_name = "new_post.html"
    fields = ['title', 'body', 'author']
    success_url = reverse_lazy("hello")


class DeletePost(DeleteView):
    model = Post
    template_name = "delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("hello")


def hello(request):
    posts = Post.objects.all()
    return render(request, "hello.html", {'post': posts})


def post_detail(request, pk):
    post = get_list_or_404(Post, id=pk)
    return render(request, 'post_detail.html', {'post': post})


class UpdatePost(UpdateView):
    model = Post
    template_name = "update_post.html"
    context_object_name = "post"
    fields = ['title', 'body']
    success_url = reverse_lazy("hello")


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = 'post'


class PostListView(ListView):
    model = Post
    template_name = "post_list.html/"
    context_object_name = 'post'


def greet(request):
    return HttpResponse("Welcome to django")


def greet2(request):
    return render(request, 'ade.html')
