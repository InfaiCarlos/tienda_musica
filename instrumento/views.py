from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Instrumento
from .forms import InstrumentoForm, InstrumentoEditarForm

def listar_instrumentos(request):
    """Página principal / Listado de registros"""
    busqueda = request.GET.get('buscar', '')
    categoria = request.GET.get('categoria', '')

    instrumentos = Instrumento.objects.all()

    if busqueda:
        instrumentos = instrumentos.filter(nombre__icontains=busqueda)
    if categoria:
        instrumentos = instrumentos.filter(categoria=categoria)

    context = {
        'instrumentos': instrumentos,
        'total': instrumentos.count()
    }
    return render(request, 'inventario/listar.html', context)

def crear_instrumento(request):
    """Formulario para Crear"""
    if request.method == 'POST':
        form = InstrumentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Instrumento registrado con éxito!')
            return redirect('listar_instrumentos')
    else:
        form = InstrumentoForm()
    return render(request, 'inventario/crear.html', {'form': form})

def editar_instrumento(request, id):
    """Formulario para Editar"""
    instrumento = get_object_or_404(Instrumento, pk=id)
    if request.method == 'POST':
        form = InstrumentoEditarForm(request.POST, instance=instrumento)
        if form.is_valid():
            form.save()
            messages.info(request, '¡Instrumento actualizado correctamente!')
            return redirect('listar_instrumentos')
    else:
        form = InstrumentoEditarForm(instance=instrumento)
    return render(request, 'inventario/editar.html', {'form': form, 'instrumento': instrumento})

def eliminar_instrumento(request, id):
    """Opción para Eliminar"""
    instrumento = get_object_or_404(Instrumento, pk=id)
    if request.method == 'POST':
        instrumento.delete()
        messages.warning(request, 'Instrumento eliminado correctamente.')
        return redirect('listar_instrumentos')
    return render(request, 'inventario/eliminar.html', {'instrumento': instrumento})