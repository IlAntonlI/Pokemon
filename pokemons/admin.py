from django.contrib import admin
from .models import Pokemon


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'gender', 'talents', 'type', 'add date')


admin.site.register(Pokemon)
