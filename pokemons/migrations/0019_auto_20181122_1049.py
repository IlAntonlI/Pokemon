# Generated by Django 2.1.3 on 2018-11-22 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0018_pokemon_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='second_name',
            new_name='last_name',
        ),
    ]