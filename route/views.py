from django.shortcuts import render
from rest_framework.views import APIView
# from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Route

def index(request):
    return HttpResponse("Hello, this is the route app.")



# class RouteDetail(APIView):
#     def get(self, request, route_id):
#         route = Route.objects.get(route_id=route_id)
#         serializer = RouteSerializer(route)
#         return Response(serializer)


# class RouteList(APIView):
#     def get(self, request):
        # user = 
        # route = Route.objects.filter(user_id=user)

        # serializer = RouteSerializer(route, many=True)
        # return Response(serializer.data)


# class RouteHashtag(APIView):
#     def post(self, request, route_id, hashtag_id):
#         route = Route.objects.get(route_id=route_id)
