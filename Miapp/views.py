from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import CategoryForm, PostForm, SearchForm
from .models import Post
from django.views.generic import DetailView
from django.views.generic import ListView


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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Se asigna el usuario logueado como autor
            post.save()
            return redirect('Miapp:home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta publicación.")
    if request.method == 'POST':
        post.delete()
        return redirect('Miapp:home')
    return render(request, 'confirm_delete.html', {'post': post})

def search_post(request):
    form = SearchForm(request.GET or None)
    results = Post.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        category = form.cleaned_data.get('category')

        if query:
            results = results.filter(title__icontains=query)

        if category:
            results = results.filter(category=category)

    return render(request, 'search_post.html', {'form': form, 'results': results})

def about(request):
    return render(request, 'about.html')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # Debes crear este template
    context_object_name = 'post'




class PagesListView(ListView):
    model = Post
    template_name = 'pages_list.html'
    context_object_name = 'posts'