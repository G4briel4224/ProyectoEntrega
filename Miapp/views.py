from django.shortcuts import render, redirect
from .forms import  CategoryForm, PostForm, SearchForm
from .models import Post
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})



@login_required
def create_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Miapp:home')
    return render(request, 'create_category.html', {'form': form})



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Usa el usuario logueado como autor
            post.save()
            return redirect('Miapp:home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def search_post(request):
    form = SearchForm(request.GET or None)
    results = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        results = Post.objects.filter(title__icontains=query)

    return render(request, 'search_post.html', {'form': form, 'results': results})


# Create your views here.
def about(request):
    return render(request, 'about.html')
