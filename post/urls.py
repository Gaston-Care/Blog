from django.urls import path
from post.views import VerDetallePublicacion, home_view, CrearPublicacion, Publicaciones, EliminarPublicacion

urlpatterns = [
    path('', home_view, name='home'),
    path('publicaciones/crear', CrearPublicacion.as_view(), name='publicaciones_crear'),
    path('publicaciones/',Publicaciones.as_view(), name='publicaciones'),
    path('publicacion/<int:pk>/', VerDetallePublicacion.as_view(), name='detalle_publicacion'),
    path('eliminar/<int:pk>/', EliminarPublicacion.as_view(), name='eliminar_publicacion'),
]