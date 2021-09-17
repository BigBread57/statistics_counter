from rest_framework import serializers

from repository_statistic.models import RepositoryStatistic


class RepositoryStatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepositoryStatistic
        fields = ('__all__',)



class RepositoryStatisticDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы со статистикой
    """

    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = RepositoryStatistic
        fields = ('date', 'views', 'clicks', 'cost', 'cpc', 'cpm')

    def get_cpc(self, obj):
        return obj.cost / obj.click

    def get_cpm(self, obj):
        return obj.cost / obj.views * 1000
