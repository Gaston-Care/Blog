from django.urls import path
from post.views import home_view, CrearPublicacion,Publicaciones

urlpatterns = [
    path('', home_view, name='home'),
    path('publicaciones/crear', CrearPublicacion.as_view(), name='publicaciones_crear'),
    path('publicaciones/',Publicaciones.as_view(), name='publicaciones'),
]