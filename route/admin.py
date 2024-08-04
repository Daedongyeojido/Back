from django.contrib import admin
from .models import Route, Place, Route_places

class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_id', 'startpoint_name', 'startpoint_address', 'startpoint_x', 'startpoint_y', 
                    'endpoint_name', 'endpoint_address', 'endpoint_x', 'endpoint_y', 'date', 'user_id')
    search_fields = ('startpoint_name', 'endpoint_name', 'date')
    list_filter = ('date', 'user_id')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_id', 'place_name', 'place_address', 'place_like', 'place_latitude', 
                    'place_longitude', 'subCategory')
    search_fields = ('place_name', 'place_address')
    list_filter = ('subCategory', 'place_like')

class RoutePlacesAdmin(admin.ModelAdmin):
    list_display = ('route_places_id', 'route', 'place', 'user_like')
    search_fields = ('route', 'place')
    list_filter = ('user_like',)

# Register the models with their respective ModelAdmin classes
admin.site.register(Route, RouteAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Route_places, RoutePlacesAdmin)
