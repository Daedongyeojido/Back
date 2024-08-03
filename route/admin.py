from django.contrib import admin
from .models import Route, Place, Route_places

class RoutePlacesInline(admin.TabularInline):
    model = Route_places
    extra = 1  # 인라인 폼의 기본 수

class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_id', 'startpoint_name', 'startpoint_address', 'endpoint_name', 'endpoint_address', 'date', 'user_id')
    search_fields = ('startpoint_name', 'endpoint_name', 'user_id__username')  # 사용자 이름으로 검색할 수 있게 설정
    inlines = [RoutePlacesInline]

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_id', 'place_name', 'place_address', 'place_like', 'place_latitude', 'place_longitude', 'subCategory')
    search_fields = ('place_name', 'place_address', 'subCategory__subCategory_name')  # 서브 카테고리 이름으로 검색할 수 있게 설정

class RoutePlacesAdmin(admin.ModelAdmin):
    list_display = ('route', 'place', 'user_like')
    search_fields = ('route__route_id', 'place__place_name')  # 경로 ID와 장소 이름으로 검색할 수 있게 설정

admin.site.register(Route, RouteAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Route_places, RoutePlacesAdmin)
