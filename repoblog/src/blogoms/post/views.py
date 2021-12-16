from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post, Ver_Post, Like, Comentario

# Create your views here.

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = (
        'titulo', 'contenido', 'thumbnail', 'autor', 'slug'
    )

class PostDeleteView(DeleteView):
    model = Post