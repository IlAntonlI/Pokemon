# Generated by Django 2.1.3 on 2018-11-14 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0011_auto_20181114_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(upload_to='images', verbose_name='Photo'),
        ),
    ]
