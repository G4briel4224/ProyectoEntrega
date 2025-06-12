from django.shortcuts import render, redirect
from .forms import AuthorForm, CategoryForm, PostForm, SearchForm
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def create_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_author.html', {'form': form})

def create_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_category.html', {'form': form})

def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_post.html', {'form': form})

def search_post(request):
    form = SearchForm(request.GET or None)
    results = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        results = Post.objects.filter(title__icontains=query)

    return render(request, 'search_post.html', {'form': form, 'results': results})


# Create your views here.
