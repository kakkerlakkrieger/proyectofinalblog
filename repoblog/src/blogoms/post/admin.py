from django.contrib import admin
from .models import Post, Comentario, Ver_Post, Like, Usuario
# Register your models here.
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Ver_Post)
admin.site.register(Like)
admin.site.register(Usuario)