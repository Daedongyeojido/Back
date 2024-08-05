from rest_framework import serializers
from .models import *
from hashtag.serializers import *

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
        fields = ['place_id', 'place_latitude', 'place_longitude', 'place_name', 'place_address', 'place_like', 'subCategory']

class RecommendationResponseSerializer(serializers.Serializer):
    map_pins = serializers.ListField(child=serializers.DictField())
    places = serializers.ListField(child=serializers.DictField())


class RouteSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)
    hashtag = HashtagSerializer(many=True, read_only=True)

    class Meta:
        model = Route
        fields = ['startpoint_name', 'startpoint_address', 'endpoint_name', 'endpoint_address', 'places', 'hashtag']

