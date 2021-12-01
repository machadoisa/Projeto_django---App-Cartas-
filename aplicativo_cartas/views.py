from django.shortcuts import render, get_object_or_404, redirect
from .forms import UsuarioForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


@login_required()
def cadastrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)

        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('cadastrar_usuario')
    else:
        form = UsuarioForm()
    return render(request, "form.html", {'form': form})

class SingUp(generic.CreativeView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'




#Add Django site authentication urls (for login, logout, password management)


