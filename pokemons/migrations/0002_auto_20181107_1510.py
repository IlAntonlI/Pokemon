# Generated by Django 2.1.3 on 2018-11-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.FloatField(),
        ),
    ]
