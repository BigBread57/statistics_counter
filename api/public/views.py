from rest_framework import viewsets, generics

from api.public.serializers import RepositoryStatisticSerializer
from repository_statistic.models import RepositoryStatistic


class RepositoryStatisticViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для статистики
    """

    queryset = RepositoryStatistic.objects.all()
    serializer_class = RepositoryStatisticSerializer


class GetStatisticDetail(generics.ListAPIView):
    """
    Набор представлений для статистики
    """

    queryset = RepositoryStatistic.objects.all()
    serializer_class = RepositoryStatisticSerializer
