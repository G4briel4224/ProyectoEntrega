from django import forms
from .models import Author, Category, Post  # Asegurate que estos modelos existen

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category']

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
