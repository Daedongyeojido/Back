from rest_framework import serializers
from .models import Category, SubCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source = 'category.category_id')

    class Meta:
        model = SubCategory
        fields = '__all__'