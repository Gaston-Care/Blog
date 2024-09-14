from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from post.models import Publicacion
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

class CrearPublicacion(LoginRequiredMixin, CreateView):
    model = Publicacion
    fields = ['titulo','contenido']
    template_name = 'crear_publicacion.html'
    success_url = reverse_lazy('publicaciones')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class Publicaciones(ListView):
    model = Publicacion
    template_name = 'publicaciones.html'

    def get_queryset(self):
        return Publicacion.objects.all()
    
class EliminarPublicacion(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('publicaciones')

    def get_queryset(self):
        return Publicacion.objects.filter(autor=self.request.user)

class VerDetallePublicacion(DetailView):
    model = Publicacion
    template_name = 'detalle_publicacion.html'

class EditarPublicacion(UpdateView):
    model = Publicacion
    fields = ['titulo','contenido']
    template_name = 'editar_publicacion.html'
