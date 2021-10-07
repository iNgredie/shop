from django.db.models import Case, When, Value, IntegerField
from django.utils.timezone import now
from django_filters import FilterSet, NumberFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from shops.api.serializers import ShopSerializer
from shops.models import Shop


class ShopFilter(FilterSet):
    open = NumberFilter(field_name="open")

    class Meta:
        model = Shop
        fields = ('street', 'city', 'open')


class ShopModelViewSet(ModelViewSet):
    """ Создание и вывод магазинов по фильтру"""

    http_method_names = ['get', 'post', 'head']
    queryset = Shop.objects.all().annotate(
        open=Case(
            When(opening_time__lte=now().time(),
                 closing_time__gte=now().time(),
                 then=Value(1)),
            default=Value(0),
            output_field=IntegerField()))
    serializer_class = ShopSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ShopFilter
