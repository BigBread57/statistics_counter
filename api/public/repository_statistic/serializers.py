from rest_framework import serializers

from repository_statistic.models import RepositoryStatistic


class RepositoryStatisticSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения информации о первоначальной информации о событии
    """

    class Meta:
        model = RepositoryStatistic
        fields = '__all__'

    def validate(self, data):
        if data.get('views') and data['views'] < 0:
            raise serializers.ValidationError("Количество просмотров должно быть целым положительным числом")
        if data.get('clicks') and data['clicks'] < 0:
            raise serializers.ValidationError("Количество кликов должно быть целым положительным числом")
        if data.get('cost') and data['cost'] < 0:
            raise serializers.ValidationError("Стоимость кликов должно быть положительным числом")
        return data


class GetStatisticSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы со статистикой по событию
    """
    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = RepositoryStatistic
        fields = ('id', 'date', 'views', 'clicks', 'cost', 'cpc', 'cpm')
        read_only_fields = ('id', 'views', 'clicks', 'cost')

    def get_cpc(self, obj):
        if obj['cost'] == 0 or obj['clicks'] == 0:
            return 0
        else:
            return float('{:.3f}'.format(obj['cost'] / obj['clicks']))

    def get_cpm(self, obj):
        if obj['cost'] == 0 or obj['views'] == 0:
            return 0
        else:
            return float('{:.3f}'.format(obj['cost'] / obj['views'] * 1000))
