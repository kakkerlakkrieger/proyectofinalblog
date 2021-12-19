from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from post.views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', PostListView.as_view(), name='lista'),
    path('create/', PostCreateView.as_view(), name='crear'),
    path('<slug>/', PostDetailView.as_view(), name='detalle'),
    path('<slug>/update', PostUpdateView.as_view(), name='actualizar'),
    path('<slug>/delete', PostDeleteView.as_view(), name='borrar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)