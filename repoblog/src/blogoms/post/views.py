from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post, Ver_Post, Like, Comentario
from .forms import PostForm, CommentForm
# Create your views here.

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comentario = form.instance
            comentario.usuario = self.request.user
            comentario.post = post
            comentario.save()
            return redirect("detalle", slug=post.slug)
        return redirect("detalle", slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context
    
    def get_object(self, **kwargs):
        object=super().get_object(**kwargs)
        # if self.request.user.is_authenticated:
        #     Ver_Post.objects.get_or_create(user=self.request.user, post=object)
        #     #Ver_Post.objects
        # return object

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'create'
        })
        return context
    # fields = (
    #     'titulo', 'contenido', 'thumbnail', 'autor', 'slug'
    # )

class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context
    # fields = (
    #     'titulo', 'contenido', 'thumbnail', 'autor', 'slug'
    # )

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'