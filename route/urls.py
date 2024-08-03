from django.urls import path
from .views import PlaceRecommendationAPIView

urlpatterns = [
    path('place-recommendations/', PlaceRecommendationAPIView.as_view(), name='place-recommendations'),
]