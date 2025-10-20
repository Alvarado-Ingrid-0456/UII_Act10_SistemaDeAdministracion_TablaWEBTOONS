from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Webtoon
from .forms import WebtoonForm
# Create your views here.

# Página principal: listar webtoons
def index(request):
    return render(request, 'webtoons/index.html', {
        'webtoons': Webtoon.objects.all()
    })

# Ver webtoon (opcional — aquí solo redirige de nuevo al index)
def ver_webtoon(request, id):
    webtoon = Webtoon.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

# Agregar un nuevo webtoon
def agregar_webtoon(request):
    if request.method == 'POST':
        form = WebtoonForm(request.POST)
        if form.is_valid():
            nuevo_titulo = form.cleaned_data['titulo']
            nuevo_genero = form.cleaned_data['genero']
            nuevo_descripcion = form.cleaned_data['descripcion']
            nuevo_estado = form.cleaned_data['estado']
            nuevo_fecha_publicacion = form.cleaned_data['fecha_publicacion']
            nuevo_portada_url = form.cleaned_data['portada_url']
            nuevo_calificacion_promedio = form.cleaned_data['calificacion_promedio']

            nuevo_webtoon = Webtoon(
                titulo=nuevo_titulo,
                genero=nuevo_genero,
                descripcion=nuevo_descripcion,
                estado=nuevo_estado,
                fecha_publicacion=nuevo_fecha_publicacion,
                portada_url=nuevo_portada_url,
                calificacion_promedio=nuevo_calificacion_promedio
            )
            nuevo_webtoon.save()
            return render(request, 'webtoons/agregar_webtoon.html', {
                'form': WebtoonForm(),
                'success': True
            })
    else:
        form = WebtoonForm()
    return render(request, 'webtoons/agregar_webtoon.html', {
        'form': form
    })

# Editar un webtoon existente
def editar_webtoon(request, id):
    if request.method == 'POST':
        webtoon = Webtoon.objects.get(pk=id)
        form = WebtoonForm(request.POST, instance=webtoon)
        if form.is_valid():
            form.save()
            return render(request, 'webtoons/editar_webtoon.html', {
                'form': form,
                'success': True
            })
    else:
        webtoon = Webtoon.objects.get(pk=id)
        form = WebtoonForm(instance=webtoon)
    return render(request, 'webtoons/editar_webtoon.html', {
        'form': form,
        'success': False
    })

# Eliminar webtoon
def eliminar_webtoon(request, id):
    if request.method == 'POST':
        webtoon = Webtoon.objects.get(pk=id)
        webtoon.delete()
    return HttpResponseRedirect(reverse('index'))
