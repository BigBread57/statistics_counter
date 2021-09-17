from django.db import models


class RepositoryStatistic(models.Model):
    """
    Модель хранит статистику о событиях
    """

    date = models.DateField('Дата события')
    views = models.IntegerField('Количество показов', blank=True, default=0)
    clicks = models.IntegerField('Количество кликов', blank=True, default=0)
    cost = models.DecimalField('Стоимость кликов в рублях', max_digits=19, decimal_places=2, blank=True, default=0)

    class Meta:
        verbose_name = 'Хранилище статистики'
        verbose_name_plural = 'Хранилище статистики'

    def __str__(self):
        return str(self.date)

