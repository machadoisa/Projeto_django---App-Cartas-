from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User





# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.ImageField(blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# logins = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')
