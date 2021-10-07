from django.db import models


class Street(models.Model):
    """ Улица """

    name = models.CharField(max_length=255, verbose_name='Название')
    city = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
        verbose_name='Город'
    )

    def __str__(self) -> str:
        return f'{self.name}'


class City(models.Model):
    """ Город """

    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self) -> str:
        return f'{self.name}'