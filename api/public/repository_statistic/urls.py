from django.urls import path
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from api.public.repository_statistic.views import RepositoryStatisticViewSet, RepositoryStatisticList, DeleteRepository

app_name = 'repository'

router = SimpleRouter()
router.register('', RepositoryStatisticViewSet, basename='repository')

urlpatterns = [
    path('list/', RepositoryStatisticList.as_view(), name='list_repository'),
    path('destroy/', DeleteRepository.as_view(), name='destroy_repository'),
    *router.urls
]
