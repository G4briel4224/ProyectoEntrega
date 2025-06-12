from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True)

# Create your models here.
