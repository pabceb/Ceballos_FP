from django import forms

class FormularioBasePaciente(forms.Form):
    nombre = forms.CharField(max_length = 20, required=False)
    apellido = forms.CharField(max_length = 20, required=False)
    dni = forms.IntegerField(required=False)
    n_afiliado = forms.CharField(max_length = 20, required=False)
    plan = forms.CharField(max_length = 10, required=False)


class FormularioCreacionPaciente(FormularioBasePaciente):
    ...

class FormularioEdicionPaciente(FormularioBasePaciente):
    ...
    

class FormularioBuscarPaciente(forms.Form):
    n_afiliado = forms.CharField(max_length = 20, required=False)