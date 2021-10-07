from django.urls import path

from addresses.api.views import CityListAPIView, StreetsInTheCityList

urlpatterns = [
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/street/', StreetsInTheCityList.as_view(), name='street_list'),
]