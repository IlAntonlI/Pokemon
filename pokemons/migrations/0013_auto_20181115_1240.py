# Generated by Django 2.1.2 on 2018-11-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0012_auto_20181114_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='photo',
            field=models.ImageField(upload_to='media/', verbose_name='Photo'),
        ),
    ]
