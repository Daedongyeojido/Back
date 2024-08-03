from django.urls import path
from .views import *

urlpatterns = [
    path('recommendations/', PlaceRecommendationAPIView.as_view(), name='place-recommendations'),
    # path('routeplaces/<int:route_places_id>/', RoutePlaceDeleteAPIView.as_view(), name='route-place-delete'),
]