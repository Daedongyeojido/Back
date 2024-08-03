from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from .models import Hashtag as Hashtag


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
