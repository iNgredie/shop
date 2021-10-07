from django.urls import path, include
from rest_framework import routers

from shops.api.views import ShopModelViewSet


router = routers.DefaultRouter()
router.register('shop', ShopModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]