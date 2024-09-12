from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from post.models import Publicacion

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

class CrearPublicacion(CreateView):
    model = Publicacion
    fields = ['titulo','contenido',]
    template_name = 'crear_publicacion.html'
    success_url = reverse_lazy('publicaciones')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)