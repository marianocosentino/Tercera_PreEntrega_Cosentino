from django.shortcuts import render
from .models import Profesor, Curso, Alumno
from .forms import ProfesorForm, CursoForm, AlumnoForm, SearchForm

# Create your views here.

def inicio(request):
    return render(request, "cursos/index.html")

def add_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfesorForm()
    return render(request, 'cursos/add_profesor.html', {'form': form})

def add_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoForm()
    return render(request, 'cursos/add_curso.html', {'form': form})

def add_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlumnoForm()
    return render(request, 'cursos/add_alumno.html', {'form': form})

def buscar(request):
    form = SearchForm(request.GET or None)
    results = []
    search_performed = False

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Curso.objects.filter(titulo__icontains=query)
        search_performed = True

    return render(request, 'cursos/buscar.html', {
        'form': form,
        'results': results,
        'search_performed': search_performed,
    })