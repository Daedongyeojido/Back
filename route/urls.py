from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('recommendations/', PlaceRecommendationAPIView.as_view(), name='place-recommendations'),
    path('routeplaces/', RemovePlaceFromRouteAPIView.as_view(), name='remove-place-from-route'),
    path('top_recommended_places/', views.top_recommended_places, name='top_recommended_places'),
    path('routes/<int:route_id>', RouteDetail.as_view(), name='routes'),
    path('routes', RouteList.as_view(), name='routes'),
    path('routes/<int:route_id>/place/<place_id>/recommend', PlaceLike.as_view())
]