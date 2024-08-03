from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from .models import Category, SubCategory



class CategorySave(APIView):
    def post(self, request):
        categorySerializer = CategorySerializer(data=request.data)

        if categorySerializer.is_valid(raise_exception=True):
            categorySerializer.save()
            return Response({"message" : request.data})
        
        

class SubCategorySave(APIView):
    def post(self, request, cId):
        category = Category.objects.get(category_id=cId)
        subCategorySerializer = SubCategorySerializer(data=request.data)

        if subCategorySerializer.is_valid(raise_exception=True):
            subCategorySerializer.save(category=category)
            return Response({"message" : request.data})
        return Response(subCategorySerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryList(APIView):
    def get(self, request):
        category = Category.objects.all()

        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)
            

class CategoryInfo(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None
    
    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
        