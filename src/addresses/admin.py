from django.contrib import admin

from addresses.models import City, Street
from shops.models import Shop

admin.site.register(City)
admin.site.register(Street)
admin.site.register(Shop)