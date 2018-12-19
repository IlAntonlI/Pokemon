from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import *

app_name = 'pokemons'

urlpatterns = [
    path('', TemplateView.as_view(template_name='pokemons/base.html')),
    path('pokemons/', PokemonListView.as_view(), name='pokemons'),
    path('create/', PokemonCreateView.as_view(), name='pokemon-create'),
    path('delete/', views.delete_objects, name='delete'),
    path('<int:pk>/', PokemonDetailView.as_view(), name='pokemon-detail'),
    path('delete/<int:pk>/', PokemonDeleteView.as_view(), name='pokemon-delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
