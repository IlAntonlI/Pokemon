# Generated by Django 2.1.3 on 2018-11-13 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0006_auto_20181113_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(upload_to='pokemons/', verbose_name='Photo'),
        ),
    ]
