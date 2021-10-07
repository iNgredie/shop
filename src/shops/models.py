from django.db import models

from addresses.models import City, Street


class Shop(models.Model):
    """ Магазин """

    name = models.CharField(max_length=255, verbose_name='Название')
    street = models.ForeignKey(
        Street,
        on_delete=models.CASCADE,
        verbose_name='Улица')
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='Город')

    house = models.CharField(max_length=20, verbose_name='Дом')
    opening_time = models.TimeField(verbose_name='Время открытия')
    closing_time = models.TimeField(verbose_name='Время закрытия')

    def __str__(self) -> str:
        return f'{self.name}'
