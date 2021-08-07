from django import forms
from . import models


class ContactForm(forms.ModelForm):
    # nombre = forms.CharField(widget=forms.TextInput(
    # attrs={"class": "form-control"}))

    class Meta:
        model = models.Contacto
        # fields = "nombre", "correo", "tipo_consulta", "mensaje", "aviso" estes es para darle el orden que yo quiero

        fields = '__all__'
        # esto es para importar todo lo que ya esta en models realizado en contacto


# se llamara el formulario que se encuentra en models para poder mostrarlo en la pagina


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = '__all__'
        # esto es para colocarle fecha al formulario de la pagina que agrega producto cargar un pluyin de llava scrip
        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }
