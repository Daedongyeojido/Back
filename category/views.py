from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from .models import Category, SubCategory



class categorySave(APIView):
    def post(self, request):
        categorySerializer = CategorySerializer(data=request.data)

        if categorySerializer.is_valid(raise_exception=True):
            categorySerializer.save()
            return Response({"message" : request.data})
        
        

class subCategorySave(APIView):
    def post(self, request):
        subCategorySerializer = subCategorySerializer(data=request.data)

        if subCategorySerializer.is_valid(raise_exception=True):
            subCategorySerializer.save()
            return Response({"message" : request.data})