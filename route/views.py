from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
import math
from collections import deque
from django.utils import timezone

def calculate_distance(coord1, coord2):
    R = 6371.0  # 지구의 평균 반지름 (km)
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def is_within_ellipse(coord, focus1, focus2, major_axis):
    dist_to_foci = calculate_distance(coord, focus1) + calculate_distance(coord, focus2)
    return dist_to_foci <= major_axis

def classify_and_sort_places(places, start_point, end_point, major_axis):
    categorized_places = {'식사': [], '휴식': [], '문화': [], '운동': []}
    
    for place in places:
        coord = (place['place_latitude'], place['place_longitude'])
        if is_within_ellipse(coord, start_point, end_point, major_axis):
            category = place.get('subCategory__category__category_name', 'Unknown')
            distance = calculate_distance(coord, start_point)
            place['distance'] = distance
            if category in categorized_places:
                categorized_places[category].append(place)
    
    for place_type in categorized_places:
        categorized_places[place_type].sort(key=lambda x: x['distance'])
    
    return categorized_places

def generate_balanced_recommendation(categorized_places, start_point, max_recommendations=5):
    queues = {k: deque(v) for k, v in categorized_places.items()}
    recommendation = []
    place_order = ['식사', '휴식', '문화', '운동']
    
    current_point = start_point
    
    while any(queues.values()) and len(recommendation) < max_recommendations:
        for place_type in place_order:
            if queues[place_type]:
                next_place = min(queues[place_type], key=lambda x: calculate_distance(current_point, (x['place_latitude'], x['place_longitude'])))
                queues[place_type].remove(next_place)
                next_place['distance_from_start'] = calculate_distance(start_point, (next_place['place_latitude'], next_place['place_longitude']))
                recommendation.append(next_place)
                current_point = (next_place['place_latitude'], next_place['place_longitude'])
                if len(recommendation) >= max_recommendations:
                    break
        if len(recommendation) >= max_recommendations:
            break
    
    return recommendation

# 추천 경로 api
class PlaceRecommendationAPIView(APIView):
    def post(self, request, format=None):
        
        user = request.user
        if not user.is_authenticated:
            return Response({'error': '인증이 필요합니다'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = RouteRecommendationInputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            start_point = (data['startpoint_x'], data['startpoint_y'])
            end_point = (data['endpoint_x'], data['endpoint_y'])
            distance_start_to_end = calculate_distance(start_point, end_point)
            major_axis = distance_start_to_end * 1.5

            # 제한된 반경 내의 장소만 검색
            radius = 10  # 반경 ( km)
            start_lat, start_lon = start_point
            lat_range = (start_lat - (radius / 110.574), start_lat + (radius / 110.574))
            lon_range = (start_lon - (radius / (111.320 * math.cos(math.radians(start_lat)))), start_lon + (radius / (111.320 * math.cos(math.radians(start_lat)))))
            
            # 제외할 카테고리 필터링
            avoid_categories = data.get('avoid_categories', [])
            if avoid_categories:
                excluded_subcategories = SubCategory.objects.filter(subCategory_name__in=avoid_categories)
                excluded_subcategory_ids = excluded_subcategories.values_list('subCategory_id', flat=True)
                
                places = Place.objects.exclude(
                    subCategory_id__in=excluded_subcategory_ids
                ).filter(
                    place_latitude__range=lat_range,
                    place_longitude__range=lon_range
                ).select_related('subCategory__category').values('place_latitude', 'place_longitude', 'place_name', 'place_address', 'subCategory__subCategory_name', 'subCategory__category__category_name')
            else:
                places = Place.objects.filter(
                    place_latitude__range=lat_range,
                    place_longitude__range=lon_range
                ).select_related('subCategory__category').values('place_latitude', 'place_longitude', 'place_name', 'place_address', 'subCategory__subCategory_name', 'subCategory__category__category_name')

            categorized_places = classify_and_sort_places(places, start_point, end_point, major_axis)
            recommendation = generate_balanced_recommendation(categorized_places, start_point, max_recommendations=5)
            
            map_pins = [{"id": i+1, "latitude": place['place_latitude'], "longitude": place['place_longitude']} for i, place in enumerate(recommendation)]
            places_response = [{"place_name": place['place_name'], "place_address": place['place_address'], "subCategory": place['subCategory__subCategory_name']} for place in recommendation]
            
            user = request.user  # 현재 로그인된 사용자
            route = Route.objects.create(
                startpoint_name=data['startpoint_name'],
                startpoint_address=data['startpoint_address'],
                startpoint_x=data['startpoint_x'],
                startpoint_y=data['startpoint_y'],
                endpoint_name=data['endpoint_name'],
                endpoint_address=data['endpoint_address'],
                endpoint_x=data['endpoint_x'],
                endpoint_y=data['endpoint_y'],
                date=timezone.now(),
                user_id=user
            )

            for place in recommendation:
                place_obj = Place.objects.get(place_name=place['place_name'], place_address=place['place_address'])
                Route_places.objects.create(route=route, place=place_obj, user_like=False)
            
            response_data = {
                "route": {
                    "map_pins": map_pins,
                    "places": places_response
                }
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 추천 경로 삭제 api
class RemovePlaceFromRouteAPIView(APIView):
    def delete(self, request, format=None):
        user = request.user
        if not user.is_authenticated:
            return Response({'error': '인증이 필요합니다'}, status=status.HTTP_401_UNAUTHORIZED)

        route_id = request.query_params.get('route_id')
        place_id = request.query_params.get('place_id')

        if not route_id or not place_id:
            return Response({'error': 'route_id와 place_id가 필요합니다'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            route = Route.objects.get(route_id=route_id, user_id=user)
            place = Place.objects.get(place_id=place_id)
        except Route.DoesNotExist:
            return Response({'error': '유효하지 않은 route_id'}, status=status.HTTP_404_NOT_FOUND)
        except Place.DoesNotExist:
            return Response({'error': '유효하지 않은 place_id'}, status=status.HTTP_404_NOT_FOUND)

        try:
            route_place = Route_places.objects.get(route=route, place=place)
            route_place.delete()
            return Response({'message': '삭제 성공'}, status=status.HTTP_200_OK)
        except Route_places.DoesNotExist:
            return Response({'error': '해당 route_id와 place_id의 연결이 존재하지 않습니다'}, status=status.HTTP_404_NOT_FOUND)

# 메인 장소 순위 api
def top_recommended_places(request):
    top_places = Place.objects.order_by('-place_like')[:3]
    places_data = [
        {
            "place_name": place.place_name,
            "place_address": place.place_address,
            "place_like": place.place_like
        }
        for place in top_places
    ]
    return JsonResponse({"top_recommended_places": places_data})