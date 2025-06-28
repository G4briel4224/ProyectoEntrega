from django.urls import path
from . import views
from .views import PagesListView

app_name = "Miapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_post/', views.create_post, name='create_post'),
    path('search/', views.search_post, name='search_post'),
    path('about/', views.about, name='about'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('detalle/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('pages/', PagesListView.as_view(), name='pages_list'),
]
