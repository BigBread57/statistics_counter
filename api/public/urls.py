from django.urls import path, include


app_name = 'public'

urlpatterns = [
    path('repository/', include('api.public.repository_statistic.urls', namespace='repository')),
]
