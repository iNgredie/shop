from rest_framework import serializers

from addresses.models import City, Street


class CitySerializer(serializers.ModelSerializer):
    """ Сериалайзер городов """

    name = serializers.CharField(required=True)

    class Meta:
        model = City
        fields = ('id', 'name')


class StreetSerializer(serializers.ModelSerializer):
    """ Сериалайзер улиц """

    name = serializers.CharField(required=True)
    city = serializers.StringRelatedField()

    class Meta:
        model = Street
        fields = ('id', 'name', 'city')