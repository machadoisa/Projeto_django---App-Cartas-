from django import forms
from aplicativo_cartas.models import Post

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'texto', 'imagem']
