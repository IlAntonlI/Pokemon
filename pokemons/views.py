from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from .forms import RegisterForm, PokemonModelForm
from .models import Pokemon


class PokemonListView(ListView):
    model = Pokemon
    template_name = 'pokemons/base.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PokemonListView, self).get_context_data(*args, **kwargs)
        context['pokemons'] = self.model.objects.all()
        return context


class PokemonCreateView(CreateView):
    model = Pokemon
    template_name = 'pokemons/pokemon_create.html'
    form_class = PokemonModelForm


class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = 'pokemons/pokemon_detail.html'


class PokemonDeleteView(DeleteView):
    model = Pokemon
    template_name = 'pokemons/pokemon_delete.html'

    def get_success_url(self):
        return reverse('pokemons:pokemons')


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'pokemons/base.html', {'form': form})
    context = {
        "form": form,
    }
    return render(request, 'pokemons/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/pokemons/')
    else:
        form = AuthenticationForm()
    return render(request, 'pokemons/login.html', {'form': form})


def logout_user(request):
    logout(request)
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'pokemons/base.html', context)


def delete_objects(request):

    if request.POST.getlist('del'):
        del_list = request.POST.getlist('del')
        Pokemon.objects.filter(pk__in=del_list).delete()
        return redirect('pokemons:pokemons')
    else:
        return redirect('/pokemons/')
