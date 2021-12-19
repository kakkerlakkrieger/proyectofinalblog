from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
#from django.shortcuts import reverse
from django.urls import reverse
# Create your models here.

class Usuario(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    thumbnail = models.ImageField()
    fecha_creado = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("detalle", kwargs={
            'slug':self.slug
        })
    @property
    def comentario (self):
        return self.comentario_set.all()
    
    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    
    @property
    def get_view_count(self):
        return self.postview_set.all().count()
    
    @property
    def get_like_count(self):
        return self.like_set.all().count()

class Comentario(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    hora = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()

    def __str__(self):
        return self.user.username
    


class Ver_Post(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    hora = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.user.username

class Like(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.user.username