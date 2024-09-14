from django.urls import path
from post.views import VerDetallePublicacion, home_view, CrearPublicacion, Publicaciones, EliminarPublicacion, EditarPublicacion

urlpatterns = [
    path('', home_view, name='home'),
    path('publicaciones/crear', CrearPublicacion.as_view(), name='publicaciones_crear'),
    path('publicaciones/',Publicaciones.as_view(), name='publicaciones'),
    path('publicaciones/<int:pk>/', VerDetallePublicacion.as_view(), name='detalle_publicacion'),
    path('publicaciones/eliminar/<int:pk>/', EliminarPublicacion.as_view(), name='eliminar_publicacion'),
    path('publicaciones/editar/<int:pk>/', EditarPublicacion.as_view(), name='editar_publicacion'),
]