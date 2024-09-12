from django.urls import path
from post.views import home_view, CrearPublicacion,publicaciones

urlpatterns = [
    path('', home_view, name='home'),
    path('crear/publicacion', CrearPublicacion.as_view(), name='crear_publicacion'),
    path('publicaciones/',publicaciones.as_view(), name='publicaciones'),
]