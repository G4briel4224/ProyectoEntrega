from django.db import models
from django.contrib.auth.models import User  # ✅ Esta línea es necesaria

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recibidos')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.remitente} a {self.destinatario}"
