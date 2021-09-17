from django.db import models


class RepositoryStatistic(models.Model):
    """
    Модель хранит статистику о событиях
    """

    date = models.DateField('Дата события', format('%Y-%m-%d'))
    views = models.IntegerField('Количество показов', blank=True)
    clicks = models.IntegerField('Количество кликов', blank=True)
    cost = models.DecimalField('Стоимость кликов в рублях', max_digits=19, decimal_places=2, blank=True)

    class Meta:
        verbose_name = 'Хранилище статистики'
        verbose_name_plural = 'Хранилище статистики'

    def __str__(self):
        return str(self.date)
