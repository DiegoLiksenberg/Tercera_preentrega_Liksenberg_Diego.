from django.shortcuts import render
from django.http import HttpResponse
from .models import Deporte, Deportista, Entrenador, Club
from .forms import DeporteForm, DeportistaForm, EntrenadorForm, ClubForm

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def deportes(request):
    contexto = {'deportes': Deporte.objects.all(), 'titulo': 'Listado de Actividades Deportivas' }
    return render(request, "aplicacion/deportes.html", contexto)

def deportistas(request):
    contexto = {'deportistas': Deportista.objects.all(), 'titulo': 'Deportistas Afiliados' }
    return render(request, "aplicacion/deportistas.html", contexto)

def entrenadores(request):
    contexto = {'entrenadores': Entrenador.objects.all(), 'titulo': 'Listado de Entrenadores' }
    return render(request, "aplicacion/entrenadores.html", contexto)

def clubes(request):
    contexto = {'clubes': Club.objects.all(), 'titulo': 'Clubes Adheridos' }
    return render(request, "aplicacion/clubes.html", contexto)

def deporteForm(request):
    if request.method == "POST":
        deporte = Deporte(nombre=request.POST['nombre'],
                          categoría=request.POST['categoría'])
        deporte.save()
        return HttpResponse("Se grabó con éxito el deporte!")
    return render(request, "aplicacion/deporteForm.html")

def deportistaForm(request):
    if request.method == "POST":
        deportista = Deportista(nombre=request.POST['nombre'],
                          apellido=request.POST['apellido'],
                          email=request.POST['email'],
                          edad=request.POST['edad'])
        deportista.save()
        return HttpResponse("Se grabó con éxito el deportista!")
    return render(request, "aplicacion/deportistaForm.html")

def entrenadorForm(request):
    if request.method == "POST":
        entrenador = Entrenador(nombre=request.POST['nombre'],
                          apellido=request.POST['apellido'],
                          email=request.POST['email'],
                          fechaAlta=request.POST['fechaAlta'])
        entrenador.save()
        return HttpResponse("Se grabó con éxito el entrenador!")
    return render(request, "aplicacion/entrenadorForm.html")

def clubForm(request):
    if request.method == "POST":
        club = Club(nombre=request.POST['nombre'],
                    domicilio=request.POST['domicilio'])
        club.save()
        return HttpResponse("Se grabó con éxito el club!")
    return render(request, "aplicacion/clubForm.html")

def deporteForm2(request):
    if request.method == "POST":
        miForm = DeporteForm(request.POST)
        if miForm.is_valid():
            deporte_nombre = miForm.cleaned_data.get('nombre')
            deporte_categoría =  miForm.cleaned_data.get('categoría')
            deporte = Deporte(nombre=deporte_nombre,
                             categoría=deporte_categoría)
            deporte.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = DeporteForm()    

    return render(request, "aplicacion/deporteForm2.html", {"form": miForm})

def deportistaForm2(request):
    if request.method == "POST":
        miForm = DeportistaForm(request.POST)
        if miForm.is_valid():
            deportista_nombre = miForm.cleaned_data.get('nombre')
            deportista_apellido =  miForm.cleaned_data.get('apellido')
            deportista_email =  miForm.cleaned_data.get('email')
            deportista_edad =  miForm.cleaned_data.get('edad')
            deportista = Deportista(nombre=deportista_nombre,
                                        apellido=deportista_apellido,
                                        email=deportista_email,
                                        edad=deportista_edad)
            deportista.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = DeportistaForm()    

    return render(request, "aplicacion/deportistaForm2.html", {"form": miForm})

def entrenadorForm2(request):
    if request.method == "POST":
        miForm = EntrenadorForm(request.POST)
        if miForm.is_valid():
            entrenador_nombre = miForm.cleaned_data.get('nombre')
            entrenador_apellido =  miForm.cleaned_data.get('apellido')
            entrenador_email =  miForm.cleaned_data.get('email')
            entrenador_fechaAlta =  miForm.cleaned_data.get('fechaAlta')
            entrenador = Entrenador(nombre=entrenador_nombre,
                                        apellido=entrenador_apellido,
                                        email=entrenador_email,
                                        fechaAlta=entrenador_fechaAlta)
            entrenador.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = EntrenadorForm()    

    return render(request, "aplicacion/entrenadorForm2.html", {"form": miForm})

def clubForm2(request):
    if request.method == "POST":
        miForm = ClubForm(request.POST)
        if miForm.is_valid():
            club_nombre = miForm.cleaned_data.get('nombre')
            club_domicilio = miForm.cleaned_data.get('domicilio')
            club = Club(nombre=club_nombre,
                       domicilio=club_domicilio)
            club.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = ClubForm()    

    return render(request, "aplicacion/clubForm2.html", {"form": miForm})

def buscarDeporte(request):
    return render(request, "aplicacion/buscarDeporte.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        deportes = Deporte.objects.filter(nombre__icontains=patron)
        contexto = {"deportes": deportes, 'titulo': f'Deportes que tienen como patrón "{patron}"'}
        return render(request, "aplicacion/deportes.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")

def buscarDeportista(request):
    return render(request, "aplicacion/buscarDeportista.html")

def buscar3(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        deportistas = Deportista.objects.filter(nombre__icontains=patron)
        contexto = {"deportistas": deportistas, 'titulo': f'Deportistas que tienen como patrón "{patron}"'}
        return render(request, "aplicacion/deportistas.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")

def buscarEntrenador(request):
    return render(request, "aplicacion/buscarEntrenador.html")

def buscar4(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        entrenadores = Entrenador.objects.filter(nombre__icontains=patron)
        contexto = {"entrenadores": entrenadores, 'titulo': f'Entrenadores que tienen como patrón "{patron}"'}
        return render(request, "aplicacion/entrenadores.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")

def buscarClub(request):
    return render(request, "aplicacion/buscarClub.html")

def buscar5(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        clubes = Club.objects.filter(nombre__icontains=patron)
        contexto = {"clubes": clubes, 'titulo': f'Clubes que tienen como patrón "{patron}"'}
        return render(request, "aplicacion/clubes.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")

