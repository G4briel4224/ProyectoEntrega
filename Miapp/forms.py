# forms.py

from django import forms
from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='Categoría'
    )
