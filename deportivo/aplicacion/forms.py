from django import forms

class DeporteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    categoría = forms.CharField(max_length=50, required=True)
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )

    turno = forms.ChoiceField(label="Turno elegido", choices=TURNOS, required=True)

class DeportistaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()
    edad = forms.IntegerField()
    federado = forms.BooleanField(required=False)

class EntrenadorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()
    fechaAlta = forms.DateField()

class ClubForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    domicilio = forms.CharField(max_length=50, required=True)
    teléfono = forms.CharField(max_length=50, required=True)