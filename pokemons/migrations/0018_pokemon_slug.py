# Generated by Django 2.1.3 on 2018-11-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0017_useraccount_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
