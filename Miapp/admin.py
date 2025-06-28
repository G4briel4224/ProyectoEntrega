
from django.contrib import admin
from .models import Post, Category  # Importa tus modelos

# Registra los modelos en el admin
admin.site.register(Post)
admin.site.register(Category)

# Register your models here.
