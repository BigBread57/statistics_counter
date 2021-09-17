from django.db.models import Q, Sum
from django.shortcuts import redirect
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.public.repository_statistic.serializers import RepositoryStatisticSerializer, GetStatisticSerializer
from repository_statistic.models import RepositoryStatistic


class RepositoryStatisticViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для события
    """

    queryset = RepositoryStatistic.objects.all()
    serializer_class = RepositoryStatisticSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        params = dict(self.request.query_params.items())
        print(params)

        if params.get('date'):
            if params.get('views') is None:
                views = 0
            else:
                views = params.get('views')
            if params.get('clicks') is None:
                clicks = 0
            else:
                clicks = params.get('clicks')
            if params.get('cost') is None:
                cost = 0
            else:
                cost = params.get('cost')
            RepositoryStatistic.objects.create(date=params.get('date'),
                                               views=views,
                                               clicks=clicks,
                                               cost=cost)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RepositoryStatisticList(generics.ListAPIView):
    """
    Представление для вывода статистики по событиям
    """

    queryset = RepositoryStatistic.objects.all()
    serializer_class = GetStatisticSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = '__all__'


    def get_queryset(self):
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        query = Q()
        if from_date:
            query = Q(query & Q(date__gte=from_date))
        if to_date:
            query = Q(query & Q(date__lte=to_date))
        if not from_date and not to_date:
            query = Q(query)
        return super().get_queryset().values('date').filter(query).annotate(views=Sum('views'),
                                                                            clicks=Sum('clicks'),
                                                                            cost=Sum('cost'))


class DeleteRepository(APIView):
    """
    Представление для уничтожения статистики
    """

    queryset = RepositoryStatistic.objects.all()

    def get(self, request, format=None):
        RepositoryStatistic.objects.all().delete()
        return redirect('/api/v1/repository')
