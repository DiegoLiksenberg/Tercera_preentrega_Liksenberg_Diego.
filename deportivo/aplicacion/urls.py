from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('deportes/', deportes, name="deportes"),
    path('deportistas/', deportistas, name="deportistas"),
    path('entrenadores/', entrenadores, name="entrenadores"),
    path('clubes/', clubes, name="clubes"),

    path('deporte_form/', deporteForm, name="deporte_form"),
    path('deportista_form/', deportistaForm, name="deportista_form"),
    path('entrenador_form/', entrenadorForm, name="entrenador_form"),
    path('club_form/', clubForm, name="club_form"),
    path('deporte_form2/', deporteForm2, name="deporte_form2"),
    path('deportista_form2/', deportistaForm2, name="deportista_form2"),
    path('entrenador_form2/', entrenadorForm2, name="entrenador_form2"),
    path('club_form2/', clubForm2, name="club_form2"),

    path('buscar_deporte/', buscarDeporte, name="buscar_deporte"),
    path('buscar2/', buscar2, name="buscar2"),

    path('buscar_deportista/', buscarDeportista, name="buscar_deportista"),
    path('buscar3/', buscar3, name="buscar3"),

    path('buscar_entrenador/', buscarEntrenador, name="buscar_entrenador"),
    path('buscar4/', buscar4, name="buscar4"),

    path('buscar_club/', buscarClub, name="buscar_club"),
    path('buscar5/', buscar5, name="buscar5"),

]
