from rest_framework import serializers
from .models import Category, SubCategory

class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source = 'category.category_id')

    class Meta:
        model = SubCategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    subCategory = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'