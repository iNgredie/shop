from rest_framework.generics import ListAPIView

from addresses.api.serializers import CitySerializer, StreetSerializer
from addresses.models import City, Street


class CityListAPIView(ListAPIView):
    """ Вывод списка городов """

    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetsInTheCityList(ListAPIView):
    """ Вывод списка городов по pk города"""

    serializer_class = StreetSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Street.objects.filter(city_id=pk)
