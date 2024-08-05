from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from .models import Hashtag as Hashtag, Route_Hashtag
from route.models import Route
from route.serializers import RouteSerializer


class HashtagView(APIView):
    def post(self, request):
        serializer = HashtagSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(request.data)
        
        return Response({"message" : "save failed"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        hashtag = Hashtag.objects.all()
        serializer = HashtagSerializer(hashtag, many=True)

        return Response(serializer.data)


class RouteHashtag(APIView):
    def post(self, request, route_id, hashtag_id):

        user = request.user
        if not user.is_authenticated:
            return Response({'error': '인증이 필요합니다'}, status=status.HTTP_401_UNAUTHORIZED)

        if not route_id or not hashtag_id:
            return Response({'error': 'route_id와 place_id가 필요합니다'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            route = Route.objects.get(route_id=route_id, user_id=user)
            hashtag = Hashtag.objects.get(id=hashtag_id)
        except Route.DoesNotExist:
            return Response({'error': '유효하지 않은 route_id'}, status=status.HTTP_404_NOT_FOUND)
        except Hashtag.DoesNotExist:
            return Response({'error': '유효하지 않은 hashtag_id'}, status=status.HTTP_404_NOT_FOUND)
        
        Route_Hashtag.objects.create(route=route, hashtag=hashtag)

        # serializer = RouteSerializer(route)
        # return Response(serializer.data)
        return Response({'message': 'hashtag updated successfully'}, status=status.HTTP_200_OK)
    
    def delete(self, request, route_id, hashtag_id):

        user = request.user
        if not user.is_authenticated:
            return Response({'error': '인증이 필요합니다'}, status=status.HTTP_401_UNAUTHORIZED)

        if not route_id or not hashtag_id:
            return Response({'error': 'route_id와 place_id가 필요합니다'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            route = Route.objects.get(route_id=route_id, user_id=user)
            hashtag = Hashtag.objects.get(id=hashtag_id)
        except Route.DoesNotExist:
            return Response({'error': '유효하지 않은 route_id'}, status=status.HTTP_404_NOT_FOUND)
        except Hashtag.DoesNotExist:
            return Response({'error': '유효하지 않은 hashtag_id'}, status=status.HTTP_404_NOT_FOUND)
        
        
        try:
            route_hashtag = Route_Hashtag.objects.get(route=route, hashtag=hashtag)
            route_hashtag.delete()
            return Response({'message': 'hashtag deleted successfully'}, status=status.HTTP_200_OK)
        except Route_Hashtag.DoesNotExist:
            return Response({'error': '해당 route_id와 hashtag_id 연결이 존재하지 않습니다'}, status=status.HTTP_404_NOT_FOUND)
