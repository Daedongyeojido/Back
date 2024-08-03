from django.contrib import admin
from .models import Route, Place, Route_places

# Route 모델을 위한 관리자 클래스
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_id', 'startpoint_name', 'startpoint_address', 'startpoint_x', 'startpoint_y', 
                    'endpoint_name', 'endpoint_address', 'endpoint_x', 'endpoint_y', 'date', 'user_id')
    search_fields = ('startpoint_name', 'endpoint_name', 'user_id__username')  # 검색 필드
    list_filter = ('date',)  # 필터링 옵션

# Place 모델을 위한 관리자 클래스
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_id', 'place_name', 'place_address', 'place_like', 'place_latitude', 'place_longitude', 'subCategory')
    search_fields = ('place_name', 'place_address', 'subcategory_id__subcategory_name')  # 검색 필드
    list_filter = ('subCategory',)  # 필터링 옵션

# Route_places 모델을 위한 관리자 클래스
class RoutePlacesAdmin(admin.ModelAdmin):
    list_display = ('route_places_id', 'route_id', 'user_like')
    search_fields = ('route_id__route_id',)  # 검색 필드
    list_filter = ('user_like',)  # 필터링 옵션

# 모델 등록
admin.site.register(Route, RouteAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Route_places, RoutePlacesAdmin)
