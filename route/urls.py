from django.urls import path
from .views import *

urlpatterns = [
    path('recommendations/', PlaceRecommendationAPIView.as_view(), name='place-recommendations'),
    path('routeplaces/', RemovePlaceFromRouteAPIView.as_view(), name='remove-place-from-route'),
]