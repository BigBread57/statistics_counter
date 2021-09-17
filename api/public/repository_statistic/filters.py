import django_filters

from repository_statistic.models import RepositoryStatistic


class RepositoryStatisticFilter(django_filters.FilterSet):
    from_date = django_filters.DateFilter(label="Начальная дата события",
                                          field_name='date', lookup_expr='gte')
    to_date = django_filters.DateFilter(label="Конечная дата события",
                                        field_name='date', lookup_expr='lte')

    class Meta:
        model = RepositoryStatistic
        fields = ['date']
