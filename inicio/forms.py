from django import forms

class FormularioCreacionPaciente(forms.Form):
    nombre = forms.CharField(max_length = 20)
    apellido = forms.CharField(max_length = 20)
    dni = forms.IntegerField()
    plan = forms.CharField(max_length = 10)
    n_afiliado = forms.IntegerField()