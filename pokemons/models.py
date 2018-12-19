from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    name = models.CharField('Имя', max_length=30)
    slug = models.SlugField()
    weight = models.FloatField('Вес')
    gender = models.CharField('Пол', max_length=30)
    talents = models.CharField('Таланты', max_length=100)
    type = models.CharField('Тип', max_length=100)
    photo = models.ImageField('Фото', upload_to='images', blank=True)
    add_date = models.DateField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.name

    # def image_(self):
    #     return '<a href="/media/{0}"><img src="/media/{0}"></a>'.format(self.photo)

    # image_.allow_tags = True

    def get_absolute_url(self):
        return reverse('pokemons:pokemon-detail', args=[str(self.id)])
