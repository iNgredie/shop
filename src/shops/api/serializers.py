from rest_framework import serializers

from addresses.models import Street
from shops.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    """ Сериалайзер магазинов """

    open = serializers.IntegerField(read_only=True)
    house = serializers.IntegerField()

    class Meta:
        model = Shop
        fields = (
            'id',
            'name',
            'street',
            'city',
            'house',
            'opening_time',
            'closing_time',
            'open'
        )

    def validate(self, data):
        queryset = Street.objects.select_related('city').filter(city_id=data['city'].id)
        if data['street'].id not in [street.pk for street in queryset]:
            raise serializers.ValidationError(f'В городе {data["city"]} нет улицы {data["street"]}')
        if data['opening_time'] > data['closing_time']:
            raise serializers.ValidationError("Время открытия должно быть меньше, чем время закрытия")
        return data
