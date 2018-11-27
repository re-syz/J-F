"""
131072
271118 - initial
geo/admins.py



"""


# =============

from django.contrib import admin
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.

class Geo_Info_Admin(admin.ModelAdmin):
    formfield_overrides = {
    map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
