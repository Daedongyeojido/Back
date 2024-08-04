from rest_framework import serializers
from .models import *

class RouteRecommendationInputSerializer(serializers.Serializer):
    startpoint_name = serializers.CharField(max_length=50)
    startpoint_address = serializers.CharField(max_length=50)
    startpoint_x = serializers.FloatField()
    startpoint_y = serializers.FloatField()
    endpoint_name = serializers.CharField(max_length=50)
    endpoint_address = serializers.CharField(max_length=50)
    endpoint_x = serializers.FloatField()
    endpoint_y = serializers.FloatField()
    avoid_categories = serializers.ListField(child=serializers.CharField(),required=False, allow_empty=True)

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['place_latitude', 'place_longitude', 'place_name', 'subcategory_id__subcategory_name']

class RecommendationResponseSerializer(serializers.Serializer):
    map_pins = serializers.ListField(child=serializers.DictField())
    places = serializers.ListField(child=serializers.DictField())
